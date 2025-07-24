#!/usr/bin/env python3
"""
Functions counts the number of vowels and consonants in a string respectively
"""

def count_vowels(sentence):
    vows = ["a", "e", "i", "o", "u"]
    num_vowels = 0
    for i in sentence.lower():
        if i in vows:
            num_vowels += 1
    return num_vowels

def count_consonants(sentence):
    vows = ["a", "e", "i", "o", "u"]
    special = "!@#$%^&*()-_+={\}[]\|;:'<,.>/?1234567890"
    num_cons = len(sentence)
    for i in sentence:
        if i in vows or i in special or " " == i:
            num_cons -= 1
    return num_cons

if __name__ == '__main__':
    sentence = "Th1s sent3nce h4s numb3rs."
    print(count_vowels(sentence))
    print(count_consonants(sentence))

