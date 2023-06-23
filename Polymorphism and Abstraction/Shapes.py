from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    def calculate_area(self):
        return math.pi * (self._radius ** 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self._radius

class Rectangle(Shape):
    def __init__(self, height, width):
        self._width = width
        self._height = height

    def calculate_perimeter(self):
        return self._width * 2 + self._height * 2

    def calculate_area(self):
        return self._width * self._height
