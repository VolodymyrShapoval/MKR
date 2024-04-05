from funcs.read_content import *


def write_to_file(content, write_file_path):
    """
    Writes the given content to a file specified by the provided path.

    Args:
        content (list or set): The content to be written to the file.
        write_file_path (str): The path to the file to write the content into.

    Raises:
        PermissionError: If the user does not have permission to write to the file.
        OSError: For any other operating system related errors.
    """
    with open(write_file_path, "w") as file:
        file.writelines(content)


def write_same_line_to_file(write_file_path, readfile1, readfile2):
    """
    Writes the lines that are present in both readfile1 and readfile2 into a file specified by write_file_path.

    Args:
        write_file_path (str): The path to the file where the common lines will be written.
        readfile1 (str): The path to the first file.
        readfile2 (str): The path to the second file.

    Raises:
        PermissionError: If the user does not have permission to write to the file.
        FileNotFoundError: If one of the input files is not found.
        UnicodeDecodeError: If there is an issue decoding the contents of the files.
        OSError: For any other operating system related errors while working with files.
    """
    same_lines = get_same_content_from_files(readfile1, readfile2)
    write_to_file(same_lines, write_file_path)


def write_diff_line_to_file(write_file_path, readfile1, readfile2):
    """
    Writes the lines that occur only in one of the input files into a file specified by write_file_path.

    Args:
        write_file_path (str): The path to the file where the different lines will be written.
        readfile1 (str): The path to the first file.
        readfile2 (str): The path to the second file.

    Raises:
        PermissionError: If the user does not have permission to write to the file.
        FileNotFoundError: If one of the input files is not found.
        UnicodeDecodeError: If there is an issue decoding the contents of the files.
        OSError: For any other operating system related errors while working with files.
    """
    diff_lines = get_different_content_from_files(readfile1, readfile2)
    write_to_file(diff_lines, write_file_path)



