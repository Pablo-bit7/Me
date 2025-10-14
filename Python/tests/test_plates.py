#!/usr/bin/env python3
"""
Tests for the Vanity Plates program
"""
from plates import is_valid


def test_valid_plates():
    """Test plates that should be valid"""
    assert is_valid("CS50") == True
    assert is_valid("ECTO88") == True
    assert is_valid("NRVOUS") == True


def test_invalid_length():
    """Test plates with invalid length"""
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False


def test_invalid_number_placement():
    assert is_valid("CS05") == False
    assert is_valid("50") == False
    assert is_valid("CS50P2") ==False


def test_invalid_characters():
    """Test plates with invalid characters"""
    assert is_valid("PI3.14") == False


if __name__ == "__main__":
    test_valid_plates()
    test_invalid_length()
    test_invalid_number_placement()
    test_invalid_characters()
