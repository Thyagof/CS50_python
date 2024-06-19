from numb3rs import validate

def test_limits():
    assert validate("255.255.255.255") == True
    assert validate("254.254.254.254") == True
    assert validate("256.256.256.256") == False

def test_partition_1():
    assert validate("9.9.9.9") == True
    assert validate("19.19.19.19") == True
    assert validate("199.199.199.199") == True

def test_range():
    assert validate("1000.1000.1000.1000") == False
    assert validate("1000.255.255.255") == False
    assert validate("75.456.76.65") == False
    assert validate("255.255.1000.255") == False
    assert validate("255.255.255.1000") == False

def test_word():
    assert validate("cat") == False

def test_format():
    assert validate("255.255.255.255.255") == False
    assert validate("255.255.255") == False
    assert validate("255.255") == False
    assert validate("255") == False