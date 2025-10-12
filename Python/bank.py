#!/usr/bin/env python3
"""
Seinfeld bank
"""


def main():
    answer = input("Greeting: ")
    value(answer)


def value(greeting):
    if "hello" in greeting.lower():
        return "$0"
    elif greeting.lower()[0] == "h":
        return "$20"
    else:
        return "$100"


if __name__ == '__main__':
    main()
