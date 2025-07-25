#!/usr/bin/env python3
"""
Function finds the greatest common denominator of 2 numbers
"""

def fibonacci(n):
    a, b = 0, 1
    if n == 0:
        return a
    elif n == 1:
        return b

    for i in range(1, n):
        a, b = b, b + a

    return b

if __name__ == '__main__':
    print(fibonacci(2))
