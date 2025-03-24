import pytest
from madcubapy.utils.numeric import is_number

def test_numeric_strings():
    assert is_number("34")
    assert is_number("34.436712612874")

def test_invalid_strings():
    assert not is_number("34s")
    assert not is_number("34,342678")
    assert not is_number("34 342678")
    assert not is_number("number")
