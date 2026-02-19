"""Base vector store class moodule.

-Author: ulken94
-Contact: bestwook7@gmail.com
"""

from abc import ABC, abstractmethod
from typing import Any, TYPE_CHECKING

from langchain_core.documents import Document


class BaseVectorStore(ABC):
    """Interface for vector stores."""

    @abstractmethod
    def add_documents(self, documents: list[Document]) -> None:
        """Add documents to the vector store."""
        pass

    @abstractmethod
    def get_retriever(
        self, k: int = 4
    ) -> Any:  # TODO: Define a proper type for the retriever
        """Returns a retriever that can be used to query the vector store.

        Args:
            k (int): The number of nearest neighbors to return. Defaults to 4.
        """
        pass

    @abstractmethod
    def clear(self) -> None:
        """Clear the vector store."""
        pass
