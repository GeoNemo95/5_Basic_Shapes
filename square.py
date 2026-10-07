from rectangle import Rectangle

class Square(Rectangle):
    """Square class that inherits from Rectangle class"""
    def __init__(self, side:float, name: str = "Square"):
        """Calls Rectangle constructor"""
        super().__init__(length=side, width=side, name=name)

    @property
    def side(self) -> float:
        """Getter for _side property"""
        return self.length

    @side.setter
    def side(self, val: float):
        """Setter for _side property"""
        if not isinstance(val, float):
            raise TypeError("Side must be a number")
        if val <= 0:
            raise ValueError("Side must be above 0")
        self._length = val
        self._width = val
