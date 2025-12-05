#!/usr/bin/env python3
"""
Tests for the `working.py` program
"""
import pytest
from working import convert


# --- Valid inputs -----------------------------------------------------------

def test_full_times_with_minutes():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("5:30 PM to 9:15 AM") == "17:30 to 09:15"


def test_without_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"


def test_mixed_formats():
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"
    assert convert("12:45 AM to 10 PM") == "00:45 to 22:00"


def test_twelve_hour_edge_cases():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"


# --- Invalid inputs ---------------------------------------------------------

def test_invalid_hour_ranges():
    with pytest.raises(ValueError):
        convert("0 AM to 5 PM")


def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("9:99 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")


def test_missing_to():
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")
    with pytest.raises(ValueError):
        convert("9 AMto5 PM")


if __name__ == "__main__":
    pytest.main([__file__])
