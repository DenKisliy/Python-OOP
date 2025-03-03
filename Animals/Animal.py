class Animal:
    def __init__(self, species):
        self.species = species

    def show_species(self):
        print(f"I'm an - { self.species }")

    def make_sound(self):
        pass