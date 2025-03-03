from Pets.Dog import Dog

class Collie(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.nature = 'clever'
        self.breed = 'Collie'

    def info(self):
        super().info()
        print(f"{self.breed} has {self.nature} nature.")