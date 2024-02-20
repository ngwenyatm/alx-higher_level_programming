#!/usr/bin/python3
"""Defines function that retuirns object as json."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object."""
    return json.dumps(my_obj)
