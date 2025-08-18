#!/usr/bin/env python3
"""
Function takes int input for mass and returns the equivalent amount of energy
"""

def einstein(m):
    return m * pow(300000000, 2)


if __name__ == '__main__':
    m = int(input("m: "))
    print(einstein(m))
