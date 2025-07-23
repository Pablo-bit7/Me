#!/usr/bin/env python3
"""
Function prints `Fizz`, `Buzz` or `FizzBuzz` if conditions are met for a number passed as an argument
"""

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

if __name__ == '__main__':
    print(fizzbuzz(15))
