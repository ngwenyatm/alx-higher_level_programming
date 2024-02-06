#!/usr/bin/python3

"""Define a Square."""


class Square:
    """a square."""

    def __init__(self, size=0):
        """Initialize new square.

        Args:
            Size of new square.
        """
        self.size = size

    @property
    def size(self):
        """ size of a side one side square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""
        return (self.__size * self.__size)
