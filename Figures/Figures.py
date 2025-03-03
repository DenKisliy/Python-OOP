from Figures.Circle import Circle
from Figures.Rectangle import Rectangle

class Figures:
    def __init__(self):
        pass

    @staticmethod
    def check_number_input(self, inform_text):
        while True:
            try:
                return float(input(inform_text))
            except ValueError:
                print("Enter number")

    @staticmethod
    def make_calculate(self):
        while True:
            try:
               return float(input(f"""Check:\n1 - for circle;\n2 - rectangle\n0 - exit\n"""))
            except ValueError:
                print("Enter number")

    def run(self):
        while True:
            check_operation = self.make_calculate(self)
            if check_operation == 0:
                break
            elif check_operation == 1:
                circle = Circle(self.check_number_input(self, "Enter radius for circle "))
                circle.ares()
                circle.length()
            elif check_operation == 2:
                rectangle = Rectangle(self.check_number_input(self, "Enter length for rectangle  "),
                                   self.check_number_input(self, "Enter width for rectangle  "))
                rectangle.ares()
                rectangle.perimeter()

