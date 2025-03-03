class Dog:
    mammal = 'canine'
    nature = ''
    breed = ''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Dog's name is {self.name} and age {self.age}.")

    def make_sound(self):
        print("Gav-gav")

