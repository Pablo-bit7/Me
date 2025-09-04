#!/usr/bin/env python3
"""
Program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
"""


def main():
    amount_due = 50

    while amount_due > 0:
        print(f"Amount due: {amount_due}")
        coin = int(input("Insert coin: "))

        if coin == 25 or coin == 10 or coin == 5:
            amount_due -= coin
        else:
            continue


if __name__ == "__main__":
    main()