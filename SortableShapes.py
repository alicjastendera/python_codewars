from abc import ABC, abstractmethod
import math


class Shape(ABC):
        
    def Area(self):
        return 0

    def __eq__(self, other):
        return self.Area() == other.Area()

    def __lt__(self, other):
        return self.Area() < other.Area()
            

class CustomShape(Shape):
    def __init__(self, area):
        self.area = area

    def Area(self):
        return self.area


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return math.pi*math.pow(self.radius, 2)


class Square(Shape):
    
    def __init__(self, side):
        self.side = side

    def Area(self):
        return math.pow(self.side,2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def Area(self):
        return self.height*self.width

class Triangle(Shape):

    def __init__(self,triangleBase, height):
        self.triangleBase = triangleBase
        self.height = height

    def Area(self):
        return self.triangleBase*self.height*0.5


