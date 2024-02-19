#!/usr/bin/python3
"""Defines a class MyList that inherits from list"""

class MyList(list):
    """sort and prints attributes of class."""

    def print_sorted(self):
        print(sorted(self))
