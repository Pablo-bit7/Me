#!/usr/bin/env python3
"""
Program prompts user for a level, `𝑛` (1 to 3) then randomly generates ten
addition problems (non-negative integers with `𝑛` digits), formatted `X + Y =`
"""
import random


def main():
    ...


def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())

            if level in range(1, 4):
                return level
            else:
                raise ValueError

        except ValueError:
            continue


def generate_integer(level):
    return random.randint(level)


if __name__ == "__main__":
    main()
