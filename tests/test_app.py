"""Tests for app.py - you'll add more!"""

from app import add, is_even, reverse_string, multiply


class TestMath:
    """Tests for math functions."""

    def test_add_positive(self):
        assert add(2, 3) == 5

    def test_add_negative(self):
        assert add(-1, -1) == -2


class TestStrings:
    """Tests for string functions."""

    def test_reverse(self):
        assert reverse_string("hello") == "olleh"

    def test_is_even(self):
        assert is_even(4) is True
        assert is_even(3) is False


class TestMultiply:
    def test_multiply_positive(self):
        assert multiply(2, 3) == 6

    def test_multiply_by_zero(self):
        assert multiply(2, 0) == 0

    def test_multiply_by_negative(self):
        assert multiply(2, -3) == -6

    def test_multiply_by_one(self):
        assert multiply(2, 1) == 2
    
    def test_multiply_by_negative_one(self):
        assert multiply(2, -1) == -2

    def test_multiply_by_large_number(self):
        assert multiply(2, 1000000) == 2000000

    def test_multiply_by_large_negative_number(self):
        assert multiply(2, -1000000) == -2000000

    def test_multiply_by_large_positive_number(self):
        assert multiply(2, 1000000) == 2000000