#!/usr/bin/python3
"""Defines text indentation function."""


def text_indentation(text):
    """prints text with 2 new lines after each of these characters: ., ? and :

    Args:
        text: The text to be printed.
    Raises:
        TypeError: If text is not string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        if char.isspace():
            continue

        print(char, end="")

        if char in ".?:":
            print("\n\n", end="")

    print()
