#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def _init_(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student."""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self._dict_

    def reload_from_json(self, json):
        """Replace all attributes of the Student."""
        for k, v in json.items():
            setattr(self, k, v)
