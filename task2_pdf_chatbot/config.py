import os
from dotenv import load_dotenv

load_dotenv()

# Groq LLM Model
GROQ_MODEL = "meta-llama/llama-4-maverick-17b-128e-instruct"

# API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
