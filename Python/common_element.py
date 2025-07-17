#!/usr/bin/env python3
"""
Function takes 2 list and returns `True` if they have at least 1 element in common.
"""

def common_element(list1, list2):
    for i in list1:
        if i in list2:
            return True
        else:
            return False

if __name__ == '__main__':
    list1 = ["cat", "apple", "horizon"]
    list2 = ["cats", "dog", "banana"]
    print(common_element(list1, list2))
