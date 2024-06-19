from working import convert
import pytest

def test_valid_formats():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("12:59 AM to 1:00 PM") == "00:59 to 13:00"
    assert convert("1:00 PM to 12:59 AM") == "13:00 to 00:59"

def test_invalid_formats():
    with pytest.raises(ValueError):
        convert("12 PM - 12 AM")

    with pytest.raises(ValueError):
        convert("12:59 AM - 1:00 PM")

def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("12:60 AM to 1:60 PM")

    with pytest.raises(ValueError):
        convert("12:6 AM to 1:6 PM")
