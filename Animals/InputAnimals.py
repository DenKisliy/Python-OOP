from Animals.Animal import Animal
from Animals.Dog import Dog
from Animals.Cat import Cat
from Car.Car import Car

def show_info(object_value):
    if isinstance(object_value, Animal):
        object_value.show_species()
        object_value.make_sound()
    else:
        print(f"Current object is not animal")

dog = Dog('Dog')
cat = Cat('Cat')
car = Car('tesla', 'x1', 2022)

show_info(dog)
show_info(cat)
show_info(car)

