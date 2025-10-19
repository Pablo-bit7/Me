#!/usr/bin/env python3
"""
Reimplementation of the `fuel` program
"""


def convert(fraction_str):
    x, y = fraction_str.split("/")
    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError
    elif x > y:
        raise ValueError
    elif x != abs(x) or y != abs(y):
        raise ValueError

    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    fraction = input("Fraction: ").strip()
    ...
