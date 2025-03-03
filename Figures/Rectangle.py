class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def ares(self):
        ares = self.length * self.width
        print ("Rectangle ares: ", ares)

    def perimeter(self):
        perimeter = 2 * (self.length + self.width)
        print ("Rectangle perimeter: ", perimeter)