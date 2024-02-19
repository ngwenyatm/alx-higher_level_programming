#!/usr/bin/python3
"""Defines a function that checks obj against a_class."""

def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj: Object being checked.
        a_class: The class to compare obj to.
    Returns:
        True if the object is exactly an instance of the specified class;
        otherwise False.
    """
    if type(obj) == a_class:
        return True
    return False
