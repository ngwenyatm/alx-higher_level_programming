#!/usr/bin/python3

"""model class called Base."""
import json

class Base:
    """Base class.

   Private Attributes:
        __nb_object: Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes an instance of Base.

        Arguments:
            id: The id for Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
