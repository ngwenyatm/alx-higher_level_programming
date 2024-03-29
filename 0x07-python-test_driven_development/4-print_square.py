#!/usr/bin/python3
"""Defines a function that prints a square with the character #."""


def print_square(size):
    """Print a square with the # character.

    Args:
        size: The length of one side of a square.
        """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
