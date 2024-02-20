#!/usr/bin/python3
"""Defines Student class and returns dict."""


class Student:
    """A student class."""

    def __init__(self, first_name, last_name, age):
        """Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dict version of instance
        """
        if isinstance(attrs, list) and all(isinstance(ele, str) for ele in attrs):

            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
