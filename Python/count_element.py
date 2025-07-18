#!/usr/bin/env python3
"""
Function returns unique elements of a list and the number of times they appear
"""
from collections import Counter

def count_element(my_list):
    counts = Counter(my_list)

    unique_elements = list(counts.keys())
    occurance = list(counts.values())

    return unique_elements, occurance

if __name__ == '__main__':
    my_list = [1, "cat", 2, "dog", 1, 2]
    unique_elements, occurance = count_element(my_list)
    
    print(f"Unique elements: {unique_elements}")
    print(f"Their respective occurances are: {occurance}")
