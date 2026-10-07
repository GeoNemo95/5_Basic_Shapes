from basic_shape import BasicShape
from circle import Circle
from rectangle import Rectangle
from square import Square

class Polymorph():
    def __init__(self):
        """creates an initial list of shape objects"""
        self.shapes = [
            Circle(radius = 10.0, name = "Circ1"),
            Circle(radius = 7.0, name = "Circ2"),
            Rectangle(length = 5.0, width = 3.0, name = "Rect1"),
            Rectangle(length = 9.0, width = 4.0, name = "Rect2"),
            Square(side = 4.0, name = "Sqre1")
        ]

    def print_shape_area(self):
        """Display name of object and the calculated area"""
        for shape in self.shapes:
            print(f"{shape.name} Area: {shape.calc_area()}")

    def modify_shape(self):
        """function to modify and display the values and calculated area of the shapes in the list"""
        print(f"--- Old values for {self.shapes[0].name} ---")
        print(f"Radius:  {self.shapes[0].radius}")
        print(f"Area:    {self.shapes[0].calc_area()}")
        self.shapes[0].radius = 5.0
        print(f"--- New values for {self.shapes[0].name} ---")
        print(f"Radius:  {self.shapes[0].radius}")
        print(f"Area:    {self.shapes[0].calc_area()}")
        
        print("----------------------------------------------")

        print(f"--- Old values for {self.shapes[3].name} ---")
        print(f"Length:  {self.shapes[3].length}")
        print(f"Width:   {self.shapes[3].width}")
        print(f"Area:    {self.shapes[3].calc_area()}")
        self.shapes[3].length = 35.0
        self.shapes[3].width = 29.0
        print(f"--- New values for {self.shapes[3].name} ---")
        print(f"Length:  {self.shapes[3].length}")
        print(f"Width:   {self.shapes[3].width}")
        print(f"Area:    {self.shapes[3].calc_area()}")

        print("----------------------------------------------")
        
        print(f"--- Old values for {self.shapes[4].name} ---")
        print(f"Radius:  {self.shapes[4].side}")
        print(f"Area:    {self.shapes[4].calc_area()}")
        self.shapes[4].side = 22.0
        print(f"--- New values for {self.shapes[4].name} ---")
        print(f"Radius:  {self.shapes[4].side}")
        print(f"Area:    {self.shapes[4].calc_area()}")

poly = Polymorph()
poly.print_shape_area()
poly.modify_shape()

