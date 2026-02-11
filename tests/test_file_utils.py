"""Test code for file utilities.

-Author: ulken94
-Contact: bestwook7@gmail.com
"""

import pytest

from utils.file_utils import read_file, split_chunks


def test_read_file(tmp_path):
    # Create a temporary file with some content
    file_path = tmp_path / "test_file.txt"
    content = "Hello, this is a test file."
    file_path.write_text(content)

    # Test reading the file
    assert read_file(str(file_path)) == content

    # Test reading a non-existent file
    with pytest.raises(FileNotFoundError):
        read_file(tmp_path / "non_existent_file.txt")


def test_split_chunks():
    text = "abcdefghijklmnopqrstuvwxyz"

    # Test splitting without overlap
    chunks = split_chunks(text, chunk_size=5, overlap=0)
    assert chunks == ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]

    # Test splitting with overlap
    chunks = split_chunks(text, chunk_size=5, overlap=2)
    assert chunks == [
        "abcde",
        "defgh",
        "ghijk",
        "jklmn",
        "mnopq",
        "pqrst",
        "stuvw",
        "vwxyz",
        "yz",
    ]

    # Test invalid chunk size
    with pytest.raises(ValueError):
        split_chunks(text, chunk_size=0)

    # Test negative overlap
    with pytest.raises(ValueError):
        split_chunks(text, chunk_size=5, overlap=-1)

    # Test overlap greater than or equal to chunk size
    with pytest.raises(ValueError):
        split_chunks(text, chunk_size=5, overlap=5)
