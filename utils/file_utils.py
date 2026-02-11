"""File utilities for the project.

-Author: ulken94
-Contact: bestwook7@gmail.com
"""

import os


def read_file(file_path: str, encoding: str = "utf-8") -> str:
    """Reads the content of a file and returns it as a string.

    Args:
        file_path (str): The path to the file to be read.
        encoding (str): The encoding of the file. Default is 'utf-8'.

    Returns:
        str: The content of the file as a string.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r", encoding=encoding) as f:
        text = f.read()
    return text


def split_chunks(text: str, chunk_size: int = 500, overlap: int = 0) -> list[str]:
    """Splits the input text into chunks of specified size with optional overlap.

    Args:
        text (str): The input text to be split.
        chunk_size (int): The size of each chunk. Default is 500.
        overlap (int): The number of overlapping characters between chunks.
                       Default is 0.

    Returns:
        list[str]: A list of text chunks.
    """
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than 0.")
    if overlap < 0:
        raise ValueError("Overlap must be non-negative.")
    if overlap >= chunk_size:
        raise ValueError("The chunk size must be greater than overlap.")

    chunks = [
        text[i : i + chunk_size] for i in range(0, len(text), chunk_size - overlap)
    ]
    return chunks
