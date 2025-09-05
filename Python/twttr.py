#!/usr/bin/env python3
"""
Program that prompts the user for a str of text and then outputs that same text but with all vowels omitted
"""


def main():
    usr_npt = input("Input: ").strip()
    output = ""

    for i in usr_npt:
        if i.lower() in ["a", "e", "i", "o", "u"]:
            i = ""
        output += i

    print(f"Output: {output}")


if __name__ == "__main__":
    main()