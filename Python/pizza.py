#!/usr/bin/env python3
"""
Program takes 1 command-line argument (name/path of CSV file) and outputs
a table formatted as ASCII
"""
import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_path = sys.argv[1]

    if not file_path.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            rows = [row for row in reader]
    except FileNotFoundError:
        sys.exit("File not found")

    print(tabulate(rows, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
