import asyncio
from playwright.async_api import async_playwright
import requests

URL = "https://httpbin.org/html"  # Dummy URL for demo
CHECK_INTERVAL = 20  # seconds
STOCK_KEYWORD = "Herman"  # Simulated "in-stock" keyword
TELEGRAM_TOKEN = "7889386017:AAHGttLKP7ltP6kmGnV6FrKmJhZQc64QBhg"
CHAT_ID = "<your_chat_id>"  # Replace with your own chat ID

async def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    try:
        response = requests.post(url, data=data)
        print(f"Telegram response: {response.text}")
    except Exception as e:
        print(f"Failed to send Telegram message: {e}")

async def check_stock(page):
    content = await page.content()
    return STOCK_KEYWORD in content

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(URL)

        while True:
            print("Checking stock...")
            if await check_stock(page):
                print("Stock detected! Sending Telegram alert.")
                await send_telegram_message("Stock available! Order now!")
                break
            else:
                print("No stock. Waiting...")
            await asyncio.sleep(CHECK_INTERVAL)

        await browser.close()

asyncio.run(main())
