#!/usr/bin/env python3
"""
Program takes 2 command-line argument (name/path of an existing, input CSV
file, & another as the ouput), and performs data cleaning & transformation
"""
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    if not input_file_path.endswith(".csv"):
        sys.exit("Input file is not a CSV file")
    elif not output_file_path.endswith(".csv"):
        sys.exit("Output file is not a CSV file")

    try:
        with open(input_file_path, newline="", encoding="utf-8") as csvfile:
            ...
    except FileNotFoundError:
        sys.exit("File not found")


if __name__ == "__main__":
    main()
