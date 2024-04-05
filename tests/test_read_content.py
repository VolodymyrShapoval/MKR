import pytest
from funcs import *


@pytest.mark.parametrize("filepath", ["test_txt_files/test_file1.txt",
                                      "test_txt_files/test_file2.txt"])
def test_read_content_from_file(filepath: str):
    result = read_content_from_file(filepath)
    assert result is not None


@pytest.mark.parametrize("filepath1, filepath2", [("test_txt_files/test_file1.txt",
                                      "test_txt_files/test_file2.txt")])
def test_get_same_content_from_files(filepath1, filepath2):
    result = get_same_content_from_files(filepath1, filepath2)
    assert result is not None

