#!/usr/bin/env python3
"""
Program expects a `str` and returns an `int` of the number of times that “um”
appears in the input, not as a substring of some other word.
"""
import re


def main():
    print(count(input("Text: ")))


def count(string):
    matches = re.findall(r"\bum\b", string, re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()
