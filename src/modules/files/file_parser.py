"""File utility module for handling file operations.

-Author: ulken94
-Contact: bestwook7@gmail.com
"""

import os

from src.modules.files import JSONLoader, PDFLoader, TxtLoader


class FileParser:
    """A utility class for parsing file."""

    def __init__(self, file_path: str) -> None:
        """Initailizes the FileParser with the given file path.

        Args:
            file_path (str): The path to the file to be parsed.
        """
        self.file_path = file_path
        self.loader: PDFLoader | JSONLoader | TxtLoader
        self._init_loader()

    def _init_loader(self) -> None:
        """Initializes the appropriate loader based on the file type."""
        if self.file_path is None:
            raise ValueError("File path is not set.")
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File '{self.file_path}' does not exist.")

        if self.file_path.endswith(".txt") or self.file_path.endswith(".TXT"):
            self.loader = TxtLoader(self.file_path)
        elif self.file_path.endswith(".json") or self.file_path.endswith(".JSON"):
            self.loader = JSONLoader(self.file_path)
        elif self.file_path.endswith(".pdf") or self.file_path.endswith(".PDF"):
            self.loader = PDFLoader(self.file_path)
        else:
            raise ValueError(f"Unsupported file type: {self.file_path}")
