#!/usr/bin/python3
# 6-from_json_string.py
"""Defines  function that returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """Return object representated by a JSON string."""
    return json.loads(my_str)
