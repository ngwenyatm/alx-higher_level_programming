#!/usr/bin/python3
"""Defines function that appends string to text file."""


def append_write(filename="", text=""):
    """Appends string to end of text file.

   Returns:
        No of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
