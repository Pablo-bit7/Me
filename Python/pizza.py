#!/usr/bin/env python3
"""
Program takes 1 command-line argument (name/path of CSV file) and outputs
a table formatted as ASCII
"""
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_path = sys.argv[1]

    if not file_path.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(file_path, newline="") as file:
            ...
    except FileNotFoundError:
        sys.exit("File not found")


if __name__ == "__main__":
    main()
