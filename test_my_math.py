import my_math


def test_add():
    assert my_math.add(7, 3) == 10
    assert my_math.add(7, -1) == 6
    assert my_math.add(4.3, 5.3) == 9.6

def test_product():
    assert my_math.product(5, 5) == 25
    assert my_math.product(5, 2.5) == 12.5

def test_invert_string():
    assert my_math.invert_string("") == ""
    assert my_math.invert_string("asd") == "dsa"

def test_is_palindrom():
    assert my_math.is_palindrom("ala") == True
    assert my_math.is_palindrom("as") == False

def test_square():
    assert my_math.square(-2) == 4
    assert my_math.square(5) == 25
    assert my_math.square(0) == 0

# test_add()
# test_product()
# test_invert_string()
# test_is_palindrom()
# Zakomentowane. Niepotrzebne, ponieważ zaczynamy używać pytest