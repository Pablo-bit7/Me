#!/usr/bin/env python3
"""
Function takes a list if strings and returns the longest string
"""

def longest_string(list):
    word = ""

    for i in list:
        if len(i) > len(word):
            word = i

    return word


if __name__ == '__main__':
    string_list = ["cat", "apple", "horizon"]
    print(longest_string(string_list))
