#!/usr/bin/python3
"""Defines a function that reads a text file (UTF8) and prints it to stdout."""


def read_file(filename=""):
    """Print the UTF8 file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
