#!/usr/bin/env python3
"""
Function counts how many ducks are being refered to in a string
"""

def count_ducks(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    count = 0
    for word in words:
        if "ducks" in word:
            count += 2
        elif "duck" in word:
            count += 1
    return count

if __name__ == '__main__':
    print(count_ducks("Python programming is fun!"))