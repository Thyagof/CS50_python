from plates import is_valid

def test_valid_plate():
    assert is_valid("CS50") == True

def test_starting_zero():
    assert is_valid("CS05") == False

def test_ending_consonant():
    assert is_valid("CS50P") == False

def test_starting_number():
    assert is_valid("12333") == False

def test_punctuation():
    assert is_valid("PI3.14") == False

def test_short_plate():
    assert is_valid("H") == False

def test_no_numbers():
    assert is_valid("OUTATIME") == False