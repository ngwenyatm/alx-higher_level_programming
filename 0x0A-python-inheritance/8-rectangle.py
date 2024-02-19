#!/usr/bin/python3
"""defines class BaseGeometry and Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representation of rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intializes Rectangle.

        Args:
            height: The height Rectangle
            width: The width of Rectangle
        """
    def __init__(self, width, height):
        """instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
