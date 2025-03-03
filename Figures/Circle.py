import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def ares(self):
        ares = math.pow(self.radius, 2) * math.pi
        print ("Circle ares: ", ares)

    def length(self):
        length = 2 * math.pi * self.radius
        print ("Circle length: ", length)

