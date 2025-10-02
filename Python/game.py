#!/usr/bin/env python3
"""
Simple guessing game
"""
import random


def main():
    while True:
        try:
            usr_npt = int(input("Level: ").strip())

            if usr_npt > 0:
                level = random.randrange(1, usr_npt + 1)

                while True:
                    try:
                        usr_guess = int(input("Guess: ").strip())

                        if usr_guess > 0:
                            if usr_guess == level:
                                print("Just right!")
                                break
                            elif usr_guess > level:
                                print("Too large!")
                                continue
                            else:
                                print("Too small!")
                                continue
                        else:
                            continue

                    except ValueError:
                        continue

                break
            else:
                continue      

        except ValueError:
            continue


if __name__ == '__main__':
    main()
