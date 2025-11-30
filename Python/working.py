#!/usr/bin/env python3
"""
Program expects a `str` representing time in 12-hour format, and then
converts and returns the corresponding `str` in 24-hour format
"""
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(time_12hr):
    try:
        ...

    except ValueError:
        sys.exit("Invalid input")


if __name__ == "__main__":
    main()
