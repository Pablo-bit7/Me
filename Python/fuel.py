#!/usr/bin/env python3
"""
Program prompts user for a fraction and outputs how much fuel is in the tank as a percentage
"""


def main():
    while True:
        fraction = input("Fraction: ").strip()

        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            perc = (x / y) * 100

        except ValueError:
            continue
        except ZeroDivisionError:
            continue

        else:
            if x > y or x < 0:
                continue
            elif perc <= 1:
                print("E")
            elif perc >= 99:
                print("F")
            else:
                print(f"{round(perc)}%")
            
            break


if __name__ == "__main__":
    main()
