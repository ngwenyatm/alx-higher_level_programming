#!/usr/bin/python3
"""function"""


def inherits_from(obj, a_class):
    """Checks if an object is inherited.

    Args:
        obj: The object
        a_class: The class
    Returns:
        True if the object is an instance of a class that inherited (directly or indirectly) from the specified class;
        otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
