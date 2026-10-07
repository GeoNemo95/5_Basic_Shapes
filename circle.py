import math
from basic_shape import BasicShape

class Circle(BasicShape):
    """Circle class that inherits from BasicShape class"""
    def __init__(self, x_center: float = 0.0, y_center: float = 0.0, radius: float = 0.0,name: str = "Circle" ):
        """Calls BasicShape constructor"""
        super().__init__(name)
        self._x_center = x_center
        self._y_center = y_center
        self._radius = radius

    @property
    def x_center(self) -> float:
        """Getter for _x_center property"""
        return self._x_center

    @property
    def y_center(self) -> float:
        """Getter for _y_center property"""
        return self._y_center

    @property
    def radius(self) -> float:
        """Getter for _radius property"""
        return self._radius

    @x_center.setter
    def x_center(self, val: float):
        """Setter for _x_center property"""
        if not isinstance(val, float):
            raise TypeError("X Coordinate must be a number")
        self._x_center = val

    @y_center.setter
    def y_center(self, val: float):
        """Setter for _y_center property"""
        if not isinstance(val, float):
            raise TypeError("Y Coordinate must be a number")
        self._y_center = val

    @radius.setter
    def radius(self, val: float):
        """Setter for _radius property"""
        if not isinstance(val, float):
            raise TypeError("Radius must be a number")
        if val <= 0:
            raise ValueError("Radius must be above 0")
        self._radius = val

    def calc_area(self):
        """Returns area of circle from the given radius"""
        return math.pi * (self.radius ** 2)


