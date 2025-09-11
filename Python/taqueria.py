#!/usr/bin/env python3
"""
Program prompts user for items on a menu and outputs the total cost
"""


def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    amount_due = 0

    while True:
        try:
            order = input("Item: ").strip()
            amount_due += menu[order.title()]
            print(f"\nTotal: ${amount_due:.2f}")

        except ValueError:
            continue
        except KeyError:
            continue
        except EOFError:
            break


if __name__ == "__main__":
    main()
