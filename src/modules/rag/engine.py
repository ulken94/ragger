"""Rag engine main class.

-Author: ulken94
-Contact: bestwook7@gmail.com
"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from src.configs.settings import Settings
from src.modules.vector_store.base_store import BaseVectorStore


class RagEngine:
    """Rag engine main class."""

    def __init__(self, vector_store: BaseVectorStore) -> None:
        """Initialize the RAG engine.

        Args:
            vector_store (BaseVectorStore): The vector store to use for retrieval.
        """
        self.vector_store = vector_store

        self.llm = ChatGoogleGenerativeAI(
            model=Settings.llm_model,
            temperature=0,
            google_api_key=Settings.google_api_key,
        )
        self.chain = None
        self._build_chain()

    def _build_chain(self) -> None:
        """Build the RAG engine chain."""
        retriever = self.vector_store.get_retriever()

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a helpful assistant that answers questions based on the provided context.",
                    "You should use the retrieved documents to answer the question as accurately as possible.",
                    "If the retrieved documents do not contain enough information to answer the question, you should say that you don't know the answer.",
                    "Answer the following question based on the retrieved documents:\n\n{context}\n\nQuestion: {question}",
                ),
                ("human", "{question}"),
            ]
        )


