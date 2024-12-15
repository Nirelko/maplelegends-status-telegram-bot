# MapleLegends Server Status Bot

This project is a Telegram bot that monitors the status of the MapleLegends game server. It scrapes the MapleLegends website periodically and sends notifications to a Telegram chat whenever the server status changes.

## Features

- Monitors the server status every 60 seconds (configurable).
- Sends the current server status when the bot starts.
- Notifies you of any status changes (e.g., Offline to Online or vice versa).

## Requirements

- Python 3.7+
- A Telegram bot token (get one from [BotFather](https://core.telegram.org/bots#botfather)).
- Your Telegram user or group chat ID (use the [Telegram API](https://core.telegram.org/bots/api#getupdates) to retrieve this).
- Access to the MapleLegends website.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/maplelegends-status-bot.git
   cd maplelegends-status-bot
   ```

2. **Create a Python Virtual Environment** (Optional but recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the root directory and add your Telegram bot token and chat ID:

   ```env
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   TELEGRAM_CHAT_ID=your_chat_id
   ```

5. **Run the Bot**

   ```bash
   python maplelegends_status_bot.py
   ```

## Configuration

- **CHECK_INTERVAL**: The time interval (in seconds) between server status checks. This can be adjusted in the `CHECK_INTERVAL` variable in the code.
- **Logging**: Logs are displayed in the console and include timestamps and error messages.

## How It Works

1. The bot scrapes the MapleLegends homepage (`https://maplelegends.com/`) for the `<font id="server_status">` tag.
2. If the server status changes, the bot sends a message to the configured Telegram chat ID.
3. On startup, the bot sends the current server status immediately.

## Example Output

### Telegram Messages:
- **Initial Status:**
  - "Initial MapleLegends server status: Offline"
- **Status Change:**
  - "MapleLegends server status changed: Online"

## Troubleshooting

- **Coroutines Not Awaited:** Ensure you are running the updated version of the script that uses `async` and `await`. Use `asyncio.run()` to execute the `monitor_server()` function.
- **Environment Variables Not Loaded:** Double-check your `.env` file and ensure `python-dotenv` is installed (`pip install python-dotenv`).
- **Invalid Chat ID:** Make sure the `CHAT_ID` in your `.env` file is correct.

## Dependencies

- [requests](https://pypi.org/project/requests/): For fetching the website.
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/): For parsing HTML.
- [python-telegram-bot](https://pypi.org/project/python-telegram-bot/): For sending messages via Telegram.
- [python-dotenv](https://pypi.org/project/python-dotenv/): For managing environment variables.

## License

This project is open-source and available under the MIT License. Feel free to use and modify it to suit your needs.

## Contributing

Pull requests are welcome! If you find a bug or have a feature request, please open an issue.

