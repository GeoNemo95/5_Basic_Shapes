from abc import ABC, abstractmethod

class BasicShape(ABC):
    """Class representing a shape"""
    
    def __init__(self, name:str):
        """Constructor for Basic Shape"""
        self._name = name
        self._area = 0.0

    @property
    def name(self) -> str:
        """Getter for _name property"""
        return self._name

    @property
    def area(self) -> float:
        """Getter for _area property"""
        return self._area

    @name.setter
    def name(self, val: str):
        """Setter for _name property"""
        if not isinstance(val, str):
            raise TypeError("Name must be a string")
        self._name = val

    @area.setter
    def area(self, val: float):
        """Setter for _area property"""
        if not isinstance(val, float):
            raise TypeError("Area must be a number")
        self._area = val
        
    @abstractmethod
    def calc_area(self):
        """Abstract method to calculate area, modified by subclasses"""
        pass
