#!/usr/bin/python3
"""
Defines class BaseGeometry and Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representation of square"""
    def __init__(self, size):
        """initialization of square"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """returns area of square"""
        return self.__size ** 2
