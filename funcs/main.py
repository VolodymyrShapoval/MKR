from funcs import *


def main():
    filepath1 = "txt_files/file1.txt"
    filepath2 = "txt_files/file2.txt"
    write_same_line_to_file("txt_files/same.txt", filepath1, filepath2)
    write_diff_line_to_file("txt_files/diff.txt", filepath1, filepath2)


if __name__ == "__main__":
    main()
