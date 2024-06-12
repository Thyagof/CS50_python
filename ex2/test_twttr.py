from twttr import shorten

def test_shorten():
    assert shorten("hey haeiouy") == "hy hy"

def test_consonant():
    assert shorten("twttrTWTTR") == "twttrTWTTR"

def test_vowe_lower():
    assert shorten("aeiou") == ""

def test_vowe_upper():
    assert shorten("AEIOU") == ""

def test_number():
    assert shorten("123") == "123"

def test_symbol():
    assert shorten("!@#$%¨&*()") == "!@#$%¨&*()"

def test_none():
    assert shorten("") == ""