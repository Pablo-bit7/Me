#!/usr/bin/env python3
"""
Program that prompts the user for a str of text and then outputs that same text but with all vowels omitted
"""


def main():
    usr_npt = input("Input: ").strip()
    print(f"Output: {shorten(usr_npt)}")


def shorten(word):
    output = ""

    for i in word:
        if i.lower() in ["a", "e", "i", "o", "u"]:
            i = ""
        output += i

    return output


if __name__ == "__main__":
    main()
