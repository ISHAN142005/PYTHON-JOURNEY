class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius**2)


def display_area(shape):
    shape_type = type(shape).__name__
    print(f"{shape_type} Area: {shape.area()}")


rect = Rectangle(10, 5)
circ = Circle(7)

display_area(rect)
display_area(circ)
