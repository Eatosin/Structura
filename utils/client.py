import os
import nest_asyncio
from dotenv import load_dotenv

# Fix for nested event loops (Crucial for PydanticAI in some envs)
nest_asyncio.apply()

# Load Env
load_dotenv()

def get_api_key():
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise ValueError("❌ Missing GEMINI_API_KEY. Add it to .env or Secrets.")
    return key
