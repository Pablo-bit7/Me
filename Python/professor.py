#!/usr/bin/env python3
"""
Program prompts user for a level, `𝑛` (1 to 3) then randomly generates ten
addition problems (non-negative integers with `𝑛` digits), formatted `X + Y =`
"""
import random


def main():
    prb_count = 0
    ans_count = 0
    n = get_level()
    score = 0

    while prb_count != 10:
        x = generate_integer(n)
        y = generate_integer(n)

        while ans_count != 3:
            try:
                ans = int(input(f"{x} + {y} = ").strip())

                if ans == (x + y):
                    score += 1
                    break
                else:
                    raise ValueError
    
            except ValueError:
                print("EEE")
                ans_count += 1
                continue

        if ans_count == 3:
            print(f"{x} + {y} = {x + y}")
        ans_count = 0

        prb_count += 1

    print(f"Score: {score}")


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
    rng_start = 10 ** (level - 1)
    rng_end = (10 ** level) - 1

    return random.randint(rng_start, rng_end)


if __name__ == "__main__":
    main()
