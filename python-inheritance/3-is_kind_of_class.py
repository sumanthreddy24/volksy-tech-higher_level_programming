#!/usr/bin/python3
"""same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """if the object is an instance"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
