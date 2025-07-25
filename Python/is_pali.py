#!/usr/bin/env python3
"""
Function takes a string and returns whether it's a palindrome or not
"""

def is_pali(sentence):
    left_buffer = 0
    right_buffer = len(sentence) - 1

    while left_buffer < right_buffer:
        if sentence[left_buffer] == sentence[right_buffer]:
            left_buffer += 1
            right_buffer -= 1
        else:
            return False

    return True

if __name__ == '__main__':
    sentence = "lol"
    print(is_pali(sentence))
