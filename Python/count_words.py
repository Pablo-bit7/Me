#!/usr/bin/env python3
"""
Function counts the number of words in a string
"""

def count_words(sentence):
    words = sentence.split()
    return len(words)

if __name__ == '__main__':
    sentence = "Hello, World!"
    print(count_words(sentence))
