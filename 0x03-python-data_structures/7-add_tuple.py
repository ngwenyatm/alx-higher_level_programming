#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lenA, lenB = len(tuple_a), len(tuple_b)
    powTuple = ((tuple_a[0] if lenA >= 1 else 0) +
                 (tuple_b[0] if lenB >= 1 else 0),
                 (tuple_a[1] if lenA >= 2 else 0) +
                 (tuple_b[1] if lenB >= 2 else 0))
    return powTuple
