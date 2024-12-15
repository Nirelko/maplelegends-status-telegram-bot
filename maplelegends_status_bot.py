import logging
import time
import requests
from bs4 import BeautifulSoup
from telegram import Bot
from telegram.error import TelegramError
from dotenv import load_dotenv
import os
import asyncio

# Load environment variables from a .env file
load_dotenv()

# Telegram bot token and chat ID are loaded from the .env file
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# Log the tokens at the start (for debugging purposes, ensure sensitive information is handled carefully in production)
logging.info(f"Loaded BOT_TOKEN: {BOT_TOKEN}")
logging.info(f"Loaded CHAT_ID: {CHAT_ID}")

# URL to check the server status
URL = 'https://maplelegends.com/'
CHECK_INTERVAL = 60  # Time between checks in seconds

def get_server_status():
    """Scrape the server status from the website."""
    try:
        # Send a GET request to the specified URL with a timeout of 10 seconds
        response = requests.get(URL, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML response using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Look for the font tag with id="server_status" to find the server status
        status_tag = soup.find('font', id='server_status')
        if status_tag:
            return status_tag.text.strip()  # Extract and return the status text
        else:
            logging.warning("Server status tag not found on the page.")
            return None
    except requests.RequestException as e:
        logging.error(f"Error fetching server status: {e}")
        return None

async def send_telegram_message(bot, message):
    """Send a message via the Telegram bot."""
    try:
        # Use the bot instance to send a message to the specified chat ID
        await bot.send_message(chat_id=CHAT_ID, text=message)
    except TelegramError as e:
        logging.error(f"Error sending message: {e}")

async def monitor_server():
    """Monitor the server status and send updates."""
    # Initialize the Telegram bot with the token
    bot = Bot(token=BOT_TOKEN)
    last_status = None  # Keep track of the last known server status

    # Send the current status when the script starts
    initial_status = get_server_status()
    if initial_status:
        await send_telegram_message(bot, f"Initial MapleLegends server status: {initial_status}")
        logging.info(f"Initial server status sent: {initial_status}")
    else:
        logging.warning("Could not fetch initial server status.")

    while True:
        # Get the current server status
        current_status = get_server_status()
        if current_status is None:
            logging.warning("Failed to retrieve server status.")
        elif current_status != last_status:
            # If the status has changed, send a notification
            if last_status is not None:
                status_message = f"MapleLegends server status changed: {current_status}"
                await send_telegram_message(bot, status_message)
                logging.info(status_message)
            last_status = current_status  # Update the last known status
        await asyncio.sleep(CHECK_INTERVAL)  # Wait before checking again

if __name__ == "__main__":
    # Configure logging to display timestamps and log levels
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Starting MapleLegends server status monitor.")

    # Run the monitoring loop
    asyncio.run(monitor_server())
