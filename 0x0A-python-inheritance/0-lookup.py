#!/usr/bin/python3
"""Defines a function object that lists attributes"""


def lookup(obj):
    """Returns a list of an object's available attributes."""
    return (dir(obj))
