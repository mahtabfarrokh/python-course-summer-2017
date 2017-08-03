from shape import Shape
from math import pi

class Circle (Shape):
    ccounter = 0
    def __init__(self, radius , c , color):
        self.radius = radius
        self.x = c.x
        self.y = c.y
        Circle.ccounter += 1
        super().__init__("circle " + str(Circle.ccounter) , color , 0)

    def area (self):
        return pi * (self.radius ** 2)

    def circumference (self):
        return 2 * pi * self.radius