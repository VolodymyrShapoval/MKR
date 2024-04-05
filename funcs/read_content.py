def read_content_from_file(filepath: str):
    """
    Reads the contents of a file and returns it as a list of lines.

    Args:
        filepath (str): The path to the file to be read.

    Returns:
        list: A list containing the lines of the file.

    Raises:
        FileNotFoundError: If the file specified by 'filepath' does not exist.
        PermissionError: If the user does not have permission to read the file.
        UnicodeDecodeError: If there's an issue decoding the file's contents.
        OSError: For any other operating system related errors.
    """
    with open(filepath, "r") as f_o:
        return f_o.readlines()


def get_same_content_from_files(filepath1, filepath2):
    """
    Reads the contents of two files and returns a set of lines that are present in both files.

    Args:
        filepath1 (str): The path to the first file.
        filepath2 (str): The path to the second file.

    Returns:
        set: A set of lines present in both the first and the second file.

    Raises:
        FileNotFoundError: If one of the files is not found.
        PermissionError: If the user does not have permission to access the files.
        UnicodeDecodeError: If there is an issue decoding the contents of the files.
        OSError: For any other operating system related errors while working with files.
    """
    file1 = read_content_from_file(filepath1)
    file2 = read_content_from_file(filepath2)
    # Search the same lines
    same_lines = set(file1) & set(file2)
    return same_lines


def get_different_content_from_files(filepath1, filepath2):
    file1 = read_content_from_file(filepath1)
    file2 = read_content_from_file(filepath2)
    # Finding lines that occur only in one of the files
    diff_lines = set(file1) ^ set(file2)
    return diff_lines
