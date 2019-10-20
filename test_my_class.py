import math

import pytest

import my_class

def test_dog_initialization():
    d = my_class.Dog("Azor")
    assert d.name == "Azor"

def test_dog_speak():
    d = my_class.Dog("Azor")
    assert d.speak() == "Hau-hau. Jestem Azor"


def test_lamp_off_initialization():
    l = my_class.Lamp()
    assert l.is_lightening() == False


def test_lamp_on_initialization():
    l = my_class.Lamp(True)
    assert l.is_lightening() == True

## Praca domowa
## Stworzyć klasę i ją przetestować

@pytest.fixture
def calc():
    calc = my_class.Calc()
    return calc

@pytest.mark.parametrize('num1, num2, res',
                         [
                             (5, 10, 15),
                             (0, 0, 0),
                             (-3, -7, -10),
                             ("ab", "cd", "abcd"),
                             ("", "", "")
                         ])
def test_calc_add_integer_and_string(num1, num2, res, calc):
    assert calc.add(num1, num2)== res

def test_calc_add_float(calc):
    assert pytest.approx(calc.add(5.2, 5.2), 0.0001) == 10.4
    assert pytest.approx(calc.add(4.23, -2.1), 0.0001) == 2.13

def test_area():
    assert pytest.approx(my_class.circle_area(1), 0.001) == math.pi
    assert my_class.circle_area(0) == 0
    assert pytest.approx(my_class.circle_area(2.1) == math.pi*(2.1**2))

def test_area_value_exception():
    with pytest.raises(ValueError):
        my_class.circle_area(-3)

def test_area_type_exception():
    with pytest.raises(TypeError):
        my_class.circle_area(3+5j)
        my_class.circle_area(True)
        my_class.circle_area("radius")

# Używamy coverage do sprawdzenia pokrycia kodu testami.