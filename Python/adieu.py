#!/usr/bin/env python3
"""
Program prompts user for names until `Ctrl+D` signal, then bids adieu
("adieu, adieu") to those names (`𝑛` names with `𝑛` - 1 commas and one `and`)
"""
#import inflect


def main():
    names = []

    while True:
        try:
            prompt = input("Name: ").strip()
            names.append(prompt.title())

        except (EOFError, IndexError):
            output = "\nAdieu, adieu, to"

            if len(names) == 1:
                output += f" {prompt.title()}"

            elif len(names) == 2:
                for i, char in enumerate(names):
                    if i == len(names) - 1:
                        output += f" and {char}"
                    elif i == len(names) - 2:
                        output += f" {char}"
                    else:
                        output += f" {char},"

            else:
                for i, char in enumerate(names):
                    if i == len(names) - 1:
                        output += f" and {char}"
                    else:
                        output += f" {char},"

            print(output)
            break


if __name__ == '__main__':
    main()
