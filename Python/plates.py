#!/usr/bin/env python3
"""
Prompts the user for a vanity plate and validates whether it meets all of the requirements
"""
import string


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) in range(2, 7):
        if s[0:2].isalpha():
            for char in s:
                if char in string.punctuation or char == " ":
                    return False

            digit_found = False
            for char in s:
                if char.isdigit():
                    digit_found = True
                elif digit_found and char.isalpha():
                    return False

            for i, char in enumerate(s):
                if char.isdigit():
                    if char == "0":
                        return False
                    break

            return True
    
    return False


if __name__ == "__main__":
    main()
