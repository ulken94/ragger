"""ChromaDB vector store implementation.

-Author: ulken94
-Contact: bestwook7@gmail.com
"""

from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document

from src.configs.settings import Settings
from .base_store import BaseVectorStore


class ChromaStore(BaseVectorStore):
    """ChromaDB vector store implementation."""

    def __init__(
        self
    ) -> None:
        """Initialize the ChromaDB vector store."""
        self.embeddings = GoogleGenerativeAIEmbeddings(
            model=Settings.google_genai_embedding_model,
        )

        self.db = Chroma(
            persist_directory='./chroma_db',
            embedding_function=self.embeddings,
            collection_name="ragger_collection"
        )

    def add_documents(self, documents: list[Document]) -> None:
        """Add documents to the ChromaDB vector store."""
        if not documents:
            print("No documents to add.")
            return
        self.db.add_documents(documents)

    def get_retriever(self, k: int = 3) -> Any:
        """Returns a retriever that can be used to query the ChromaDB vector store."""
        return self.db.as_retriever(
            search_type="similarity",
            search_kwargs={"k": k},
        )

    def clear(self) -> None:
        """Clear the ChromaDB vector store."""
        self.db.delete_collection()
