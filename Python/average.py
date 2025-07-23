#!/usr/bin/env python3
"""
Function calculates the average of a list of numbers
"""

def average(numbers):
    sum = 0

    for i in numbers:
        sum += i

    average = sum / len(numbers)
    return average

if __name__ == '__main__':
    numbers = [1, 2, 3, 4]
    print(average(numbers))
