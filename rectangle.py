from basic_shape import BasicShape

class Rectangle(BasicShape):
    """Rectangle class that inherits from BasicShape class"""
    def __init__(self, length: float, width: float, name):
        """Calls BasicShape constructor"""
        super.()__init__("Rectangle")
        self.name = name
        self._length = length
        self._width = width

    @property
    def length(self) -> float:
        """Getter for _length property"""
        return self._length

    @property
    def width(self) -> float:
        """Getter for _width property"""
        return self._width

    @length.setter
    def length(self, val: float):
        """Setter for _length property"""
        if not isinstance(val, float):
            raise TypeError("Length must be a number")
        if val <= 0:
            raise ValueError("Length must be above 0")
        self._length = val

    @width.setter
    def width(self, val: float):
        """Setter for _width property"""
        if not isinstance(val, float):
            raise TypeError("Width must be a number")
        if val <= 0:
            raise ValueError("Width must be above 0")
        self._width = val
