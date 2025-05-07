# Author: ChatGPT

import os
from dotenv import load_dotenv
import logging

load_dotenv()

FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")
BASE_URL = "https://finnhub.io/api/v1/quote"


async def get_current_price(session, symbol: str) -> str:
    url = f"{BASE_URL}?symbol={symbol}&token={FINNHUB_API_KEY}"
    logging.info(f"Fetching current price for {symbol} url = {url}")
    async with session.get(url) as response:
        data = await response.json()

    if "c" not in data:
        return f"Error fetching data for {symbol}"
    formatted = (
        f"Current price: ${data['c']}\n"
        f"Open: ${data['o']}\n"
        f"High: ${data['h']}\n"
        f"Low: ${data['l']}"
    )
    logging.info(f"API response for {symbol}: {formatted}")
    return formatted
