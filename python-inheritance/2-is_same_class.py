#!/usr/bin/python3
"""exact same object"""


def is_same_class(obj, a_class):
    """if the object is exactly an instance of the specified class"""
    if type(obj) == a_class:
        return True
    else:
        return False
