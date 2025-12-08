#!/usr/bin/env python3
"""
Program expects a `str` and returns an `int` of the number of times that “um”
appears in the input, not as a substring of some other word.
"""
import re
import sys


def main():
    try:
        print(count(input("Text: ")))
    except ValueError:
        sys.exit("Invalid input")


def count(string):
    match = re.search(r"\bum\b", string, re.IGNORECASE)

    if not match:
        raise ValueError
    
    groups = match.groups()

    count =  0

    for i in groups:
        count += 1

    return count


if __name__ == "__main__":
    main()
