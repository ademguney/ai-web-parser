import os 
from dotenv import load_dotenv

load_dotenv()

# Ollama and OpenAI models
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1:latest")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")