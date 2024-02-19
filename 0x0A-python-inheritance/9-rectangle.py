#!/usr/bin/python3
"""class Rectangle inherited from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry class."""

    def __init__(self, width, height):
        """Intialize new Rectangle.
        """
        super().integer_validator("height", height)
        self.__height = height
        super().integer_validator("width", width)
        self.__width = width

    def area(self):
        """Return area."""
        return self.__width * self.__height

    def __str__(self):
        """Return print() and str()."""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
