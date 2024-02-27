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
    @height.setter
    def height(self, height):
        self.__height = height
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        self.__width = width
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        self.__y = y
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

