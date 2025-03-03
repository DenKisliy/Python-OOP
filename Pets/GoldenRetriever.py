from Pets.Dog import Dog

class GoldenRetriever(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.nature = 'noble'
        self.breed = 'Golden Retriever'

    def info(self):
        super().info()
        print(f"{self.breed} has {self.nature} nature.")