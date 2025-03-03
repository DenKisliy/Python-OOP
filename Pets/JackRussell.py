from Pets.Dog import Dog

class JackRussell(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.nature = 'energetic'
        self.breed = 'Jack Russell'

    def info(self):
        super().info()
        print(f"{self.breed} has {self.nature} nature.")