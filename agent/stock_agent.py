# Author: ChatGPT
from pathlib import Path
import asyncio
import aiohttp
import logging
from langchain_ollama import OllamaLLM
from tools.current_price import get_current_price
from tools.summary_tool import get_stock_summary

logging.basicConfig(level=logging.INFO)

llm = OllamaLLM(
    model="llama3.2",
    temperature=0.0,
    top_p=0.0
)


async def get_stock_info(symbol, months):
    async with aiohttp.ClientSession() as session:
        current_price_task = asyncio.create_task(get_current_price(session, symbol))
        summary_task = asyncio.create_task(get_stock_summary(session, symbol, months))

        current_price, summary = await asyncio.gather(current_price_task, summary_task)

        return current_price, summary  # returning a tuple


def extract_field(text, field_name):
    import re
    match = re.search(f"{field_name}: \\$(\\d+\\.\\d+)", text)
    value = match.group(1) if match else "N/A"
    logging.info(f"Extracted {field_name}: {value}")
    return value


def format_with_prompt(symbol, company_name, months, current_info, summary_info):
    logging.info(f"Formatting final report for {symbol}")
    prompt_template = Path("prompts/format_prompt.txt").read_text()
    filled_prompt = prompt_template \
        .replace("[Company Name]", company_name) \
        .replace("[Stock Symbol]", symbol.upper()) \
        .replace("[X]", str(months)) \
        .replace("[Price]", extract_field(current_info, "Current price")) \
        .replace("[Open]", extract_field(current_info, "Open")) \
        .replace("[High]", extract_field(current_info, "High")) \
        .replace("[Low]", extract_field(current_info, "Low")) \
        .replace("[Summary Info]", summary_info)

    response = llm(filled_prompt)  # or just print it directly!
    logging.info("Prompt ready for final LLM call")
    return response
