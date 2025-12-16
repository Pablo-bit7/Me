#!/usr/bin/env python3
"""
Program prompts user for their date of birth (`YYYY-MM-DD` format), then prints
how old they are in minutes, rounded to the nearest integer, using English
words instead of numerals
"""
import sys
import datetime
import inflect


def main():
    try:
        date_str = input("Date of Birth: ").strip()

        date_obj = validate_date(date_str)
        print(convert_to_string(date_obj))

    except ValueError:
        sys.exit("Invalid date")


def validate_date(date_str):
    """
    Validate a YYYY-MM-DD date string and return a datetime.date object.
    """
    return datetime.date.fromisoformat(date_str)


def convert_to_string(date_obj):
    """
    Convert an integer number of minutes to English words.
    """
    birth_date_midnight = datetime.datetime.combine(
        date_obj,
        datetime.time()
    )

    today_midnight = datetime.datetime.combine(
        datetime.date.today(),
        datetime.time()
    )

    delta = today_midnight - birth_date_midnight
    minutes = int(delta.total_seconds() / 60)
    p = inflect.engine()
    sentence = p.number_to_words(minutes, andword="")

    return f"{sentence.capitalize()} minutes"


if __name__ == "__main__":
    main()
