"""Base loader class module.

-Author: ulken94
-Contact: bestwook7@gmail.com
"""

import os
from abc import ABC, abstractmethod

from langchain_core.documents import Document


class BaseLoader(ABC):
    """Base loader class."""

    def __init__(
        self,
        file_path: str,
        encoding: str = "utf-8",
    ) -> None:
        """Initialize the loader.

        Args:
            file_path (str): The path to the file to load.
            encoding (str): The encoding of the file. Defaults to "utf-8".
        """
        self.file_path: str = file_path
        self.encoding = encoding

    @abstractmethod
    def load(self) -> list[Document]:
        """Load documents."""
        pass

    def _check_file(self, ext: str) -> None:
        """Check if the file exists and is accessible."""
        if not self.file_path.endswith(ext) or not self.file_path.endswith(ext.upper()):
            raise ValueError(f"File must be a {ext} file.")
        if not self._check_existance():
            raise FileNotFoundError(
                f"File {self.file_path} does not exist or is not accessible."
            )

    def _check_existance(self) -> bool:
        """Check if the file exists and is accessible."""
        return os.path.isfile(self.file_path) and os.access(self.file_path, os.R_OK)
