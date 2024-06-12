from fuel import convert
from fuel import gauge
import pytest

def test_str_convert():
    assert convert("1/2") == 50

def test_x_not_int():
    with pytest.raises(ValueError):
        convert("x/2")

def test_y_not_int():
    with pytest.raises(ValueError):
        convert("1/y")

def test_x_greater_than_y():
    with pytest.raises(ValueError):
        convert("2/1")

def test_y_equal_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0") 

def test_gauge():
    assert gauge(2) == "2%"

def test_E():
    assert gauge(1) == "E"

def test_zero():
    assert gauge(0) == "E"

def test_F():
    assert gauge(99) == "F"

def test_hundred():
    assert gauge(100) == "F"