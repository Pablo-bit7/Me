#!/usr/bin/env python3
"""
Function returns the sum of all even numbers in a list.
"""

def sum_even_numbers(num_list):
    sum = 0

    for i in num_list:
        if i % 2 == 0:
            sum += i

    return sum

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(sum_even_numbers(nums))
