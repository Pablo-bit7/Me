#!/usr/bin/env python3
"""
Program expects a `str` input and validates whether it is a syntactically valid
email address
"""
import validators


def main():
    email = input("What's your enail address? ").strip()
    
    if validate(email):
        print("Valid")
    else:
        print("Invalid")


def validate(email):
    return bool(validators.email(email))


if __name__ == "__main__":
    main()
