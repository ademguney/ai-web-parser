# WebScraper AI 🕸️🤖

An intelligent, modular, and LLM-integrated web scraping framework.

WebScraper AI enables structured data extraction from any website using either traditional scraping (Selenium with ChromeDriver) or advanced scraping (Bright Data Scraping Browser). Extracted HTML content is then processed using powerful LLMs such as OpenAI or local Ollama models.


# 📂 Project Architecture
``` bash
webscraper_ai/
│
├── app/ 🧠                         # Application logic (use cases, LLM parsing)
│   └── use_cases/
│       └── parsing/
│           ├── ollama_parser.py 🦙    # Ollama LLM parser
│           └── openai_parser.py 💬   # OpenAI GPT parser
│
├── infrastructure/ 🌐              # External systems and integrations
│   └── scraping/
│       ├── brightdata_scraper.py 🛡️   # CAPTCHA-resistant scraping
│       ├── chrome_scraper.py 🕸️      # Headless ChromeDriver scraper
│       └── utils.py 🧹               # HTML cleaner and text splitter
│
├── tests/ 🧪                      # Unit and integration tests
│   └── unit/
│       └── scraping/
│           └── test_utils.py ✅     # Tests for HTML/text utilities
│
├── interfaces/ 🚀                 # Entry points (CLI, API)
│   └── cli/
│       └── main.py 🧾              # CLI script to trigger scraping/parsing
│
├── config/ ⚙️                    # Environment and settings
│   └── settings.py 🛠️            # Loads model and scraper config from .env
├── drivers/ 🧰
│   └── chromedriver.exe 🔧        # ChromeDriver binary for local scraping
├── .env 🔐                        # Environment secrets (ignored by Git)
├── requirements.txt 📦            # Python dependencies
├── Dockerfile 🐳                  # Deployment container configuration
└── README.md 📖                   # Project documentation


```


---

## 🚀 Features

- 🧠 DOM parsing powered by OpenAI GPT or local Ollama LLMs
- 🕷️ Basic web scraping using ChromeDriver (headless)
- 🛡️ CAPTCHA-resistant scraping via Bright Data Scraping Browser
- 🧹 HTML cleaner and content splitter utilities
- ✅ Fully testable with Pytest

---



## ⚙️ Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/webscraper_ai.git
cd webscraper_ai
```

### Install dependencies
``` bash
pip install -r requirements.txt

```

### Create a .env file
``` bash
OPENAI_API_KEY=
SBR_WEBDRIVER=
OLLAMA_MODEL=llama3.1:latest
OPENAI_MODEL=gpt-4o
CHROMEDRIVER_PATH=drivers/chromedriver.exe

```

---

## 🧩 Dependencies

This project relies on the following Python libraries:

### 🔍 Web Scraping
- `selenium` – browser automation
- `beautifulsoup4`, `lxml`, `html5lib` – HTML parsing engines
- `undetected-chromedriver` – evades bot detection
- `python-dotenv` – environment variable management

### 🧠 LLM & Parsing
- `openai` – access to models
- `langchain`, `langchain-core`, `langchain-community` – LLM orchestration framework
- `langchain-openai`, `langchain-ollama` – LangChain integrations
- `ollama` – local LLM runtime

### 🖥️ Web UI (optional)
- `streamlit` – interactive UI for local testing or visualization

### 🧹 HTML Post-Processing
- `html2text` – converts HTML to plain text
- `tqdm` – progress bars during long-running tasks
- `requests` – simple HTTP requests

### ⚙️ Config & Utilities
- `pydantic` – type-safe settings and data validation


