# 🧠 Personal AI Stock Agent (Offline, LLM-Powered)

This is a local, privacy-respecting AI agent built using **Ollama (LLaMA 3.2)** and open-source tools. It allows you to ask about the **current stock price** and a **summary of historical performance** for major companies like Apple, Meta, Microsoft, and more.

---

## 🔍 Features

- ✅ Runs **locally** using `ollama` with LLaMA 3.2
- 📈 Gets **current stock price** using [Twelve Data API](https://twelvedata.com/)
- 🕒 Returns a **summary of past N months' stock trend**
- 🛠️ Uses **LangChain** to interface with the local LLM
- ⚡️ Fetches data using **parallel async requests** for performance
- 🧪 Fully modular and extensible
- 📜 Logs every step for transparency and debugging

---

## 🧱 Architecture Overview

```text
User Input (e.g., "Show me Apple stock for 3 months")
    │
    ▼
Parse Symbol & Duration (app.py)
    │
    ▼
Async get_stock_info(symbol, months)
    ├─> get_current_price(symbol)
    └─> get_stock_summary(symbol, months)
             (Both via Twelve Data API)
    │
    ▼
Format into structured prompt (format_prompt.txt)
    │
    ▼
Run prompt through LLaMA 3.2 via Ollama
    │
    ▼
Return Answer to Terminal
```

📁 Project Structure

```
ai_stock_agent/
├── app.py                     # Main CLI app
├── agent/
│   └── stock_agent.py         # Agent logic using LangChain + LLM
├── tools/
│   ├── price_tool.py          # Gets real-time stock price
│   └── summary_tool.py        # Gets N-month historical summary
├── prompts/
│   └── format_prompt.txt      # Prompt template for LLM
├── .env                       # Contains API keys
└── README.md                  # This file
```

⚙️ Setup Instructions
1. ✅ Prerequisites
- Python 3.10+
- Ollama with llama3 model installed:

    ```
    ollama pull llama3
    ```
- Get a free Twelve Data API key: https://twelvedata.com/
- Get a free Finnhub Data API key: https://finnhub.io/

2. 🧪 Install Dependencies
    ```
    pip install -r requirements.txt
   ```
   If requirements.txt is not present, install manually:

    ```
    pip install aiohttp langchain langchain-community langchain-ollama python-dotenv
    ```
3. 🔐 Setup .env File
   Create a .env file in the root directory:
- FINNHUB_API_KEY=your_finhnhubkey
- TWELVE_DATA_API_KEY=your_twelvedata_api_key
🚀 Run the Agent

    ```
    python app.py
    ```
You'll be prompted:

```text
Welcome to your Local Stock Agent 🧠

Ask me about a stock (or type 'exit'):
Input - Meta 3 months
----------------------------------------------------------------------
🧾 Stock Report:
📊 Meta (META)
Current Price: $587.31 (Open: $592.525, High: $596.03, Low: $586.58)

📈 Summary (Last 3 Months):
The stock has decreased from N/A to $587.31 over the last 3 months. It peaked at $736.67 and dipped as low as $484.66.

----------------------------------------------------------------------
Input - Accenture 6 months
----------------------------------------------------------------------
🧾 Stock Report:
📊 Accenture (ACN)
Current Price: $303.8 (Open: $303.86, High: $305.95, Low: $303.2)

📈 Summary (Last 6 Months):
The stock has decreased from N/A to $303.80 over the last 6 months. It peaked at $398.25 and dipped as low as N/A.
```

Natural language response from LLaMA

🤝 Acknowledgements
- Ollama
- Twelve Data
- Finnhub
- LangChain

📜 License
This project is open-source under the MIT License.