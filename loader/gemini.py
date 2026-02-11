"""Gemeni protocol handler for loading gemini models.

-Author: ulken94
-Contact: bestwook7@gmail.com
"""

import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyD10B-BFIx9ORy_CKHG-h3njahn9m-n9aQ"

import google.generativeai as genai


class GeminiEmbedder:
    """Gemini embedding model handler."""

    def __init__(
        self,
        model: str = "models/gemini-embedding-001",
        api_key: str | None = None,
    ) -> None:
        """Initialize the GeminiEmbedder.

        Args:
            model (str): The name of the Gemini embedding model.
            api_key (str | None): The API key for Google Generative AI.
                                 If None, it will use the environment variable.
        """
        if api_key:
            genai.configure(api_key=api_key)
        else:
            genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

        self.model = model


if __name__ == "__main__":
    get_embedding_from_gemini_model(
        model="models/gemini-embedding-001",
        content="Hello, world!",
    )
