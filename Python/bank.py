#!/usr/bin/env python3
"""
Seinfeld bank
"""

if __name__ == '__main__':
    answer = input("Greeting: ")

    if "hello" in answer.lower():
        print("$0")
    elif "h" in answer.lower():
        print("$20")
    else:
        print("$100")
