
# Purchase Bot Demo

This is a Python-based Telegram notification bot that simulates monitoring stock on a product page and sends a Telegram alert if stock is available.

## Features
- Uses Playwright to open and check a web page every 20 seconds
- Detects keyword to simulate "in-stock" behavior
- Sends Telegram message via Bot API when stock is found

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set your Telegram chat ID
Replace `<your_chat_id>` in `purchase_bot_demo.py` with your actual Telegram ID.

You can get it using @userinfobot on Telegram.

### 3. Run the bot
```bash
python purchase_bot_demo.py
```

## Screenshot
![screenshot](screenshot.png)

## Notes
- This is a prototype. You should update the URL, keyword, and element selectors based on the actual store page structure.
