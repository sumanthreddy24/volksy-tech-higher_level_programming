#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def _init_(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the Student."""
        return self._dict_
