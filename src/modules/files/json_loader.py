"""JSON loader for rag system.

-Author: ulken94
-Contact: bestwook7@gmail.com
"""

import json

from langchain_core.documents import Document

from .base_loader import BaseLoader


class JSONLoader(BaseLoader):
    """JSON loader for the rag system."""

    def __init__(self, file_path: str, encoding: str = "utf-8") -> None:
        """Initialize the loader.

        Args:
            file_path (str): The path to the JSON file to load.
            encoding (str): The encoding of the JSON file. Defaults to 'utf-8'.
        """
        super().__init__(file_path, encoding)
        self._check_file("json")

    def load(self) -> list[Document]:
        """Load a JSON file and return a list of Document objects.

        Returns:
            list[Document]: A list of Document objects containing the content of the JSON file.
        """
        try:
            with open(self.file_path, "r", encoding=self.encoding) as f:
                data = json.load(f)
            text_content = json.dumps(data, ensure_ascii=False, indent=2)
            return [
                Document(page_content=text_content, metadata={"source": self.file_path})
            ]
        except Exception as e:
            print(f"Failed to load JSON file: {e}")
            return []
