"""Gemeni protocol handler for loading gemini models.

-Author: ulken94
-Contact: bestwook7@gmail.com
"""

import os
from typing import Union

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
        self.embedding_task = "retrieval_document"

    def embed(self, text: Union[str, list[str]]) -> list[float]:
        """Get the embedding of given text.

        Args:
            text (str): The input text to embed.

        Returns:
            list[float]: The embedding vector.
        """
        result = genai.embed_content(
            model=self.model,
            content=text,
            task_type=self.embedding_task,
        )
        return result['embedding']


if __name__ == "__main__":
    gemini_embedder = GeminiEmbedder()

    sample_text = "Hello, world!"
    embedding = gemini_embedder.embed(sample_text)
    print(f"Embedding for '{sample_text}': {embedding}")

    sample_texts = ["Hello, world!", "How are you?"]
    embeddings = gemini_embedder.embed_batch(sample_texts)
    print(f"Embeddings for {sample_texts}: {embeddings}")
