#!/usr/bin/env python3
"""
Program takes 1 command-line argument (name/path of file) and outputs
the number of lines of code in the file (excluding comments and blank lines)
"""
import sys
import os


def main():
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        sys.exit("File does not exist")

    if not file_path.endswith(".py"):
        sys.exit("Not a python file")

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
    except (OSError, IOError):
        sys.exit("Could not read file")

    num_lines = 0

    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            num_lines += 1

    print(num_lines)


if __name__ == "__main__":
    main()
