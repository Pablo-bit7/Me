#!/usr/bin/env python3
"""
Program prompts user for their date of birth (`YYYY-MM-DD` format), then prints
how old they are in minutes, rounded to the nearest integer, using English
words instead of numerals
"""
import sys
import inflect
import validators
from datetime import date


def main():
    try:
        date = input("Date of Birth: ").strip()

        if validate_date(date):
            print(convert_to_string(date))
        else:
            raise ValueError

    except ValueError:
        sys.exit("Invalid date")


def validate_date(date):
    ...


def convert_to_string(date):
    ...


if __name__ == "__main__":
    main()
