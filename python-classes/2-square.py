#!/usr/bin/python3
"""size validation"""


class Square:
    """square validation"""
    def __init__(self, size=0):
        """constructor"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self .__size = size
