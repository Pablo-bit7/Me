#!/usr/bin/env python3
"""
Function takes an integer and returns `True` if it is a prime, and `False` otherwise
"""
import math

def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
        
    return True

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for i in numbers:
        print(is_prime(i))
