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
    matches = re.findall(r"\bum\b", string, re.IGNORECASE)
    
    count = len(matches)

    return count


if __name__ == "__main__":
    main()
