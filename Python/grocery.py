#!/usr/bin/env python3
"""
Program prompts user for grocery items, then outputs grocery list in uppercase, alphabetically
"""


def main():
    grocery_list = {}

    while True:
        try:
            item = input("").strip().upper()
    
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
    
        except EOFError:
            print("")
            sorted_grocery_list = dict(sorted(grocery_list.items()))

            for key, value in sorted_grocery_list.items():
                print(f"{value} {key}")

            break


if __name__ == "__main__":
    main()
