# Author: ChatGPT
import asyncio
import logging
from agent.stock_agent import format_with_prompt
from agent.stock_agent import get_stock_info

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def run():
    logging.info("App started")
    print("Welcome to your Local Stock Agent 🧠")
    print("Supported companies: Apple, Meta, Microsoft, Accenture")
    print("Example: 'Show me 3-month summary of Apple'\n")

    while True:
        query = input("Ask me about a stock (or type 'exit'): ")
        if query.lower() in {"exit", "quit"}:
            logging.info("Exiting app")
            break

        months = 3
        for word in query.split():
            if word.isdigit():
                months = int(word)
                logging.info(f"Parsed months from input: {months}")
                break

        symbol_map = {
            "apple": "AAPL",
            "meta": "META",
            "microsoft": "MSFT",
            "accenture": "ACN"
        }

        company = None
        for name in symbol_map:
            if name in query.lower():
                company = name.capitalize()
                break

        if not company:
            logging.warning("Could not detect company")
            print("❗ Please mention Apple, Meta, Microsoft, or Accenture.")
            continue

        symbol = symbol_map[company.lower()]
        logging.info(f"Processing request for {company} ({symbol})")

        try:
            current_info, summary_info = asyncio.run(get_stock_info(symbol, months))
            formatted = format_with_prompt(symbol, company, months, current_info, summary_info)
            print(f"\n🧾 Stock Report:\n{formatted}")
        except Exception as e:
            logging.error(f"Error during processing: {e}")
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    run()
