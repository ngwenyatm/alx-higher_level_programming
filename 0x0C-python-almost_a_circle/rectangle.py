#!/usr/bin/python3
"""Rectangle class based on Base"""
from models.base import Base

class Rectangle(Base):
    """Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        Args:
            id: id of rectangle
            width: Width of Rectangle
            height: height of Rectangle
            x: the x coordinate
            y: the y coordinate
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @property
    def y(self):
        return self.__y

    @property
    def x(self):
        return self.__x

    @height.setter
    def height(self, height):
        self.__height = height

    @width.setter
    def width(self, width):
        self.__width = width

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y




