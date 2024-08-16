class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def double_area(self):
        return 3.14 * self.radius * self.radius


# Creating objects of the classes
rectangle = Rectangle(5, 3)
circle = Circle(2)

shapes = [rectangle, circle]

for shape in shapes:
    print(shape.area())
