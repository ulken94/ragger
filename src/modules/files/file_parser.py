"""File utility module for handling file operations.

-Author: ulken94
-Contact: bestwook7@gmail.com
"""

import json
import os

from langchain_community.document_loaders import (
    CSVLoader,
    PyPDFLoader,
    TextLoader,
)
from langchain_core.documents import Document


class FileParser:
    """A utility class for parsing file."""

    def __init__(self, file_path: str) -> None:
        """Initializes the FileParser with the given file path.

        Args:
            file_path (str): The path to the file to be parsed.
        """
        self.file_path = file_path

    def read_file(self) -> list[Document]:
        """Reads the content of the file.

        Returns:
            str: The content of the file.

        Raises:
            FileNotFoundError: If the file does not exist.
            IOError: If there is an error reading the file.
        """
        if self.file_path is None:
            raise ValueError("File path is not set.")
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File '{self.file_path}' does not exist.")

        if self.file_path.endswith(".txt"):
            return self._read_text_file()
        elif self.file_path.endswith(".json"):
            return self._read_json_file()
        elif self.file_path.endswith(".csv"):
            return self._read_csv_file()
        elif self.file_path.endswith(".pdf"):
            return self._read_pdf_file()
        else:
            raise ValueError(f"Unsupported file type: {self.file_path}")

    def _read_text_file(self) -> list[Document]:
        """Reads a text file and returns its content as a list of Document objects.

        Returns:
            list[Document]: A list of Document objects containing
            the content of the text file.
        """
        loader = TextLoader(self.file_path, encoding="utf-8")
        return loader.load()

    def _read_json_file(self) -> list[Document]:
        """Reads a JSON file and returns its content as a list of Document objects.

        Returns:
            list[Document]: A list of Document objects containing
            the content of the JSON file.
        """
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            text_content = json.dumps(data, indent=2, ensure_ascii=False)
            # return [Document(page_content=json.dumps(data))]
            return [
                Document(
                    page_content=text_content, metadata={"source": self.file_path}
                )
            ]

    def _read_csv_file(self) -> list[Document]:
        """Reads a CSV file and returns its content as a list of Document objects.

        Returns:
            list[Document]: A list of Document objects containing
            the content of the CSV file.
        """
        loader = CSVLoader(self.file_path, encoding="utf-8")
        return loader.load()

    def _read_pdf_file(self) -> list[Document]:
        """Reads a PDF file and returns its content as a list of Document objects.

        Returns:
            list[Document]: A list of Document objects containing
            the content of the PDF file.
        """
        loader = PyPDFLoader(self.file_path)
        return loader.load()
