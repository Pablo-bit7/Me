#!/usr/bin/env python3
"""
Function returns the 2nd smallest element of a list of integers
"""

def second_smallest(numbers):
    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        return None

    unique_numbers.sort()

    return unique_numbers[1]

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(second_smallest(numbers))
