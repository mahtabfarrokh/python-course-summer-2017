from circle import Circle
from coorddinate import Coordinate

center = Coordinate(3, 4)
myCircle = Circle(1, center, "red")

print("area: ", myCircle.area())
print("circumference: ",myCircle.circumference())
print("color: ",myCircle.color)
print("side: ",myCircle.side)