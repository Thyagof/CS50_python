from project import valid_gen
from project import get_gen_index
from project import get_pokemon
from project import Pokemon

def test_valid_gen():
    assert valid_gen(0) == False
    assert valid_gen(1) == True
    assert valid_gen(2) == True
    assert valid_gen(8) == True
    assert valid_gen(9) == True
    assert valid_gen(10) == False
    assert valid_gen(1,1) == True
    assert valid_gen(1,0) == False
    assert valid_gen(1,2) == True
    assert valid_gen(9,8) == False
    assert valid_gen(9,9) == True
    assert valid_gen(9,10) == False

def test_get_gen_index():
    assert get_gen_index(1,1) == (1, 150)
    assert get_gen_index(1,2) == (1, 251)
    assert get_gen_index(2,2) == (151, 251)
    assert get_gen_index(8,8) == (810, 905)
    assert get_gen_index(8,9) == (810, 1025)
    assert get_gen_index(9,9) == (906, 1025)

def test_get_pokemon():
    assert isinstance(get_pokemon("pikachu"), Pokemon)
    assert get_pokemon("piskachu") == None
    assert isinstance(get_pokemon(1), Pokemon)
    assert get_pokemon(1233) == None