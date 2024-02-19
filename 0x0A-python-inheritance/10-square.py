#!/usr/bin/python3
"""Defines square, a Rectangle subclass"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents square."""

    def __init__(self, size):
        """Initialize square.

           size: Size of new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
