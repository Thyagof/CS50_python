from bank import value

def test_hello():
    assert value("Hello, test") == 0

def test_h():
    assert value("hi, test") == 20

def test_any():
    assert value("no hello for you") == 100