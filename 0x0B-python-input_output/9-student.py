#!/usr/bin/python3
"""
Defines student class and creates instance"
"""
class Student:
    """a class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self):
        """Returns instance of student class"""
        return self.__dict__
