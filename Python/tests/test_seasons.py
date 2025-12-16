#!/usr/bin/env python3
"""
Tests for the `seasons.py` program
"""
import pytest
import datetime
from seasons import validate_date, convert_to_string


# Tests for validate_date

def test_validate_date_valid():
    """Valid date should return a datetime.date object."""
    result = validate_date("2000-01-01")
    assert result == datetime.date(2000, 1, 1)


def test_validate_date_leap_year():
    """Leap year dates should be accepted."""
    result = validate_date("2020-02-29")
    assert result == datetime.date(2020, 2, 29)


def test_validate_date_invalid_format():
    """Invalid formats should raise ValueError."""
    with pytest.raises(ValueError):
        validate_date("01-01-2000")


def test_validate_date_invalid_date():
    """Impossible dates should raise ValueError."""
    with pytest.raises(ValueError):
        validate_date("2023-02-30")


def test_validate_date_non_date_string():
    """Non-date strings should raise ValueError."""
    with pytest.raises(ValueError):
        validate_date("hello-world")


# Tests for convert_to_string

def test_convert_to_string_zero():
    """Zero minutes should be handled correctly."""
    assert convert_to_string(0) == "zero"


def test_convert_to_string_simple_number():
    """Small numbers should be converted correctly."""
    assert convert_to_string(5) == "five"


def test_convert_to_string_large_number():
    """Large numbers should be converted correctly."""
    assert convert_to_string(525600) == (
        "five hundred twenty five thousand six hundred"
    )


def test_convert_to_string_no_and():
    """Output should not contain the word 'and'."""
    result = convert_to_string(110)
    assert "and" not in result


def test_convert_to_string_negative():
    """Negative values should raise ValueError."""
    with pytest.raises(ValueError):
        convert_to_string(-1)


if __name__ == "__main__":
    pytest.main([__file__])
