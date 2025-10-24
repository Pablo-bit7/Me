#!/usr/bin/env python3
"""
Program takes 1 command-line argument (name/path of a file) and opuputs
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

    if not os.path.endswith(".py"):
        


if __name__ == "__main__":
    main()
