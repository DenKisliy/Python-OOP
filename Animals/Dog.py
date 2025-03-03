from Animals.Animal import Animal

class Dog(Animal):
    def __init__(self, species):
        super().__init__(species)

    def make_sound(self):
        print("Woof! Woof!")