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