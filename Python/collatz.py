#!/usr/bin/env python3
"""
Function takes a number and applies the collatz conjecture to it and returns all steps 
"""

def collatz(num):
    steps = [num]

    while num != 1:
        if num % 2 == 0:
            num = num // 2
            steps.append(num)
        else:
            num = 3 * num + 1
            steps.append(num)

    return steps


if __name__ == '__main__':
    print(collatz(3))