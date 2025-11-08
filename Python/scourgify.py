#!/usr/bin/env python3
"""
Program takes 2 command-line argument (name/path of an existing, input CSV
file, & another as the ouput), and performs data cleaning & transformation
"""
import sys
import csv


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
            reader = csv.DictReader(csvfile)

            with open(output_file_path, "w", newline="", encoding="utf-8") as outfile:
                writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
                writer.writeheader()

                for i in reader:
                    full_name = i["name"]
                    house = i["house"]
                    surname, name = [part.strip() for part in full_name.split(",")]

                    writer.writerow({
                        "first": name,
                        "last": surname,
                        "house": house
                    })

    except FileNotFoundError:
        sys.exit("Input file not found")


if __name__ == "__main__":
    main()
