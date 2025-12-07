#!/usr/bin/env python3
"""
Tests for the `um.py` program
"""
import pytest
from um import count


def test_single_um():
    assert count("um") == 1


def test_single_um_with_caps():
    assert count("Um") == 1
    assert count("UM") == 1


def test_um_in_sentence():
    assert count("Um, I am thinking") == 1
    assert count("I said um.") == 1
    assert count("Well, um... okay") == 1


def test_multiple_um():
    assert count("um um") == 2
    assert count("Um, um, UM!") == 3


def test_um_with_punctuation():
    assert count("um?") == 1
    assert count("um!") == 1
    assert count("(um)") == 1
    assert count("...um...") == 1


def test_no_false_substring_matches():
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("umbrella") == 0
    assert count("vacuum") == 0
    assert count("humble") == 0


def test_um_as_part_of_hyphenated_or_joined_words():
    assert count("um-um") == 2
    assert count("um.um") == 2
    assert count("um/um") == 2
    assert count("um,um") == 2


def test_um_at_boundaries():
    assert count("um at start") == 1
    assert count("ending with um") == 1
    assert count("in the middle um yeah") == 1


def test_no_um():
    assert count("") == 0
    assert count("hello world") == 0
    assert count("I am thinking") == 0


if __name__ == "__main__":
    pytest.main([__file__])
