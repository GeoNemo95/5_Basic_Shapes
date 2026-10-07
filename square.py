from rectangle import Rectangle

class Square(Rectangle):
    """Square class that inherits from Rectangle class"""
    def __init__(self, side:float, name: str = "Square"):
        """Calls Rectangle constructor"""
        super().__init__(name, length=side, width=side)
        self._name = name
        self._side = side

    @property
    def side(self) -> float:
        """Getter for _side property"""
        return self._side

    @side.setter
    def side(self, val: float):
        """Setter for _side property"""
        if not isinstance(val, float):
            raise TypeError("Side must be a number")
        if val <= 0:
            raise ValueError("Side must be above 0")
        self._side = val
