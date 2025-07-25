import os 
from dotenv import load_dotenv

load_dotenv()

# Ollama and OpenAI models
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1:latest")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")

# Bright Data WebDriver address
SBR_WEBDRIVER = os.getenv("SBR_WEBDRIVER")

CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH", os.path.join(os.getcwd(), "drivers", "chromedriver"))
