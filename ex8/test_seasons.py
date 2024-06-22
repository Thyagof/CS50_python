from seasons import check_birthday
import pytest

def test_valid_format():
    assert check_birthday("1995-06-29") == ("1995", "06", "29")

def test_invalid_formats():
    assert check_birthday("1995-6-9") == None
    assert check_birthday("1995/06/29") == None
    assert check_birthday("1995.06.29") == None
    assert check_birthday("June 29, 1995") == None
    assert check_birthday("29/06/1995") == None
    assert check_birthday("06/29/1995") == None
    