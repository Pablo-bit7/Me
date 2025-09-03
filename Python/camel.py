#!/usr/bin/env python3
"""
Program prompts user for a variable in camel case and outputs the corresponding name in snake case
"""


def main():
    var_name = input("camelCase: ")
    snake_var = ""

    for i in var_name:
        if i.isupper():
            i = "_" + i.lower()
        snake_var += i

    print(f"snake_case: {snake_var}")


if __name__ == "__main__":
    main()
