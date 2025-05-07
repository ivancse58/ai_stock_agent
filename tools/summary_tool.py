# Author: ChatGPT

import logging
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

TWELVE_DATA_API_KEY = os.getenv("TWELVE_DATA_API_KEY")
SUMMARY_URL = "https://api.twelvedata.com/time_series"


async def get_stock_summary(session, symbol: str, months: int = 3) -> str:
    logging.info(f"Fetching summary for {symbol} over {months} month(s)")

    end_date = datetime.now()
    start_date = end_date - timedelta(days=30 * months)

    params = {
        "symbol": symbol,
        "interval": "1day",
        "start_date": start_date.strftime("%Y-%m-%d"),
        "end_date": end_date.strftime("%Y-%m-%d"),
        "apikey": TWELVE_DATA_API_KEY,
        "format": "JSON"
    }

    async with session.get(SUMMARY_URL, params=params) as response:
        data = await response.json()
    if "values" not in data:
        logging.error(f"API error for {symbol}: {data}")
        return "No data available."

    try:
        prices = [float(day["close"]) for day in data["values"]]
    except (KeyError, ValueError) as e:
        logging.error(f"Failed to parse closing prices for {symbol}: {e}")
        return "Invalid price data."

    start = prices[-1]
    end = prices[0]
    high = max(prices)
    low = min(prices)

    trend = "increased" if end > start else "decreased"
    summary = (
        f"The stock has {trend} from ${start:.2f} to ${end:.2f} over the last {months} months. "
        f"It peaked at ${high:.2f} and dipped as low as ${low:.2f}."
    )
    logging.info(f"Summary for {symbol}: {summary}")
    return summary
