#!/usr/bin/env python3
"""
Program prompts user for a fraction and outputs how much fuel is in the tank as a percentage
"""


def main():
    while True:
        fraction = input("Fraction: ").strip()
        try:
            x = int(fraction[0])
            y = int(fraction[2])
            perc = (x / y) * 100
            if y != 4:
                raise ValueError
        except ValueError:
            continue
        except ZeroDivisionError:
            continue
        else:
            if x > y:
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
