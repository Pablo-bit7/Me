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

def test_convert_to_string_known_date():
    """
    Known date should return correct age in minutes as words.
    """
    dob = datetime.date(1999, 1, 1)
    result = convert_to_string(dob)

    assert result == (
        "Fourteen million, one hundred seventy-eight thousand, "
        "two hundred forty minutes"
    )


def test_convert_to_string_today():
    """
    If date of birth is today, age should be zero minutes"""
    today = datetime.date.today()
    assert convert_to_string(today) == "Zero minutes"


def test_convert_to_string_no_and():
    """
    Output should not contain the word 'and'"""
    dob = datetime.date(2000, 1, 1)
    result = convert_to_string(dob)

    words = result.split()
    assert "and" not in words


def test_convert_to_string_type_error():
    """
    Non-date inputs should raise TypeError"""
    with pytest.raises(TypeError):
        convert_to_string(525600)


if __name__ == "__main__":
    pytest.main([__file__])
