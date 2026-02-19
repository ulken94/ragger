"""Configuration settings for the application.

-Author: ulken94
-Contact: bestwook7@gmail.com
"""

import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Configuration settings for the application."""

    google_api_key: str = os.getenv("GOOGLE_API_KEY", "")
    google_genai_embedding_model: str = "models/gemini-embedding-001"
    llm_model: str = 'models/gemini-2.5-flash'
