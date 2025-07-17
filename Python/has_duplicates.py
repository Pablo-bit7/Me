#!/usr/bin/env python3
"""
Function returns `True` if a list has duplicate elements.
"""

def check_duplicate(list):
    if len(list) != len(set(list)):
        return True
    else:
        return False

if __name__ == '__main__':
    list = ["cat", "dog", 1, 5, 1]
    print(check_duplicate(list))
