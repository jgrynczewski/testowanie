
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"Hau-hau. Jestem {self.name}"

    def rename(self, new_name):
        self.name = new_name


class Lamp:
    def __init__(self, light=False):
        self.light = light

    def turn_on(self):
        self.light = True

    def turn_off(self):
        self.light = False

    def is_lightening(self):
        return self.light