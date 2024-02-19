#!/usr/bin/python3
"""class Rectangle inherited from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class BaseGeometry:
    """Class with public methods area and integer_validator"""

    def __init__(self):
        pass

    def integer_validator(cls, name, value):
        """checks that value is greater than 0"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def area(self):
        """Raises exception when called"""
        raise NotImplementedError("area() is not implemented")


class Rectangle(BaseGeometry):
    """A representation of a rectangle"""

    def __init__(self, width, height):
        """rectangle initialization"""
        super().__init__()
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns area"""
        return self.__width * self.__height

    def __str__(self):
        """string representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
