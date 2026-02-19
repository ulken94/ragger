"""Text file loader for the rag system.

-Author: ulken94
-Contact: bestwook7@gmail.com
"""

from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document

from .base_loader import BaseLoader


class TxtLoader(BaseLoader):
    """Text file loader for the rag system."""

    def __init__(self, file_path: str, encoding: str = "utf-8") -> None:
        """Initialize the loader.

        Args:
            file_path (str): The path to the text file to load.
            encoding (str): The encoding of the text file. Defaults to 'utf-8'.
        """
        super().__init__(file_path, encoding)
        self._check_file(".txt")

    def load(self) -> list[Document]:
        """Load a text file and return a list of Document objects.

        Returns:
            list[Document]: A list of Document objects containing the content of the text file.
        """
        try:
            loader = TextLoader(self.file_path, encoding=self.encoding)
            return loader.load()
        except Exception as e:
            print(f"Failed to load text file: {e}")
            return []
