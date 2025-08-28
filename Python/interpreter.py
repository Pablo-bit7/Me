#!/usr/bin/env python3
"""
Math interpreter
"""

def interpreter(expression):
    expression_parts = expression.strip().split(" ")

    if expression_parts[1] == "+":
        answer = int(expression_parts[0]) + int(expression_parts[2])
        return f"{answer:.1f}"
    elif expression_parts[1] == "-":
        answer = int(expression_parts[0]) - int(expression_parts[2])
        return f"{answer:.1f}"
    elif expression_parts[1] == "*":
        answer = int(expression_parts[0]) * int(expression_parts[2])
        return f"{answer:.1f}"
    elif expression_parts[1] == "/":
        answer = int(expression_parts[0]) / int(expression_parts[2])
        return f"{answer:.1f}"


if __name__ == "__main__":
    while True:
        usr_npt = input("Expression: ")
        print(interpreter(usr_npt))
