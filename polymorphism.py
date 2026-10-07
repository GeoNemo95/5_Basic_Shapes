from basic_shape import BasicShape
from circle import Circle
from rectangle import Rectangle
from square import Square

class Polymorph():
    def __init__(self):
        self.shapes = [
            Circle(radius = 10.0),
            Circle(radius = 7.0),
            Rectangle(length = 5.0, width = 3.0),
            Rectangle(length = 9.0, width = 4.0),
            Square(side = 4.0)
        ]

    def print_areas(self):
        for shapes in self.shapes:
            shapes_name = type(shapes).__name__
            print(f"{shapes_name} Area: {shapes.calc_area():.2f}")

poly = Polymorph()
print(f"Shape list test: {poly.print_areas()}")

