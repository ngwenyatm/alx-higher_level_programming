#!/usr/bin/python3
"""Defines function that writes into a file"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.
        Returns number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
