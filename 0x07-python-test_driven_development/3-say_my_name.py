#!/usr/bin/python3
"""Defines a function that prints fullname."""


def say_my_name(first_name, last_name=""):
    """Print first and last names.

    Args:
        first_name: Subject first name.
        last_name: Subject last name.
    Raises:
        TypeError: If neither first_name nor last_name are strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
