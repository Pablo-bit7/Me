#!/usr/bin/env python3
"""
Function that takies an integer and returns True if it is even, False otherwise.
"""

def is_even(n):
        if n % 2 == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    try:
        n = int(input("Enter a number: "))
        print(is_even(n))
    except ValueError:
        print("Please enter a valid integer.")
