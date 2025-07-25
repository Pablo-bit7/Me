#!/usr/bin/env python3
"""
Function finds the greatest common denominator of 2 numbers
"""

def gcd(x, y):
    x_divisors = []
    y_divisors = []
    common_divi = []

    if x + y == 0:
        return 0
    elif x == 0 and y > x:
        return y
    elif y == 0 and x > y:
        return x
    
    for i in range(1, x + 1):
        if x % i == 0:
            x_divisors.append(i)

    for i in range(1, y + 1):
        if y % i == 0:
            y_divisors.append(i)

    for i in x_divisors:
        if i in y_divisors:
            common_divi.append(i)

    return max(common_divi)

if __name__ == '__main__':
    print(gcd(18, 12))
