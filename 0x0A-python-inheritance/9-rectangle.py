#!/usr/bin/python3
"""class Rectangle inherited from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().__init__()
        self.__width = integer_validator("width", width)
        self.__height = integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
