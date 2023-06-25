class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class AreaCalculator:
    def __init__(self, shapes):
        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes  # List of objects

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calculate_area()
        return total

    def __repr__(self):
        return f'The result of the calculation is: {self.total_area}'


class Square:
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side


# shapes = [Rectangle(2, 3), Rectangle(1, 6)]
# calculator = AreaCalculator(shapes)
# print("The total area is: ", calculator.total_area)
# #
# shapes = [Rectangle(10, 5), Square(10)]
# calc = AreaCalculator(shapes)
# print(calc)
# #
