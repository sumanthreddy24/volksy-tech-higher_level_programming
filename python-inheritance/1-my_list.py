#!/usr/bin/python3
"""interhitance"""


class MyList(list):
    """creater te inheritance"""
    def print_sorted(self):
        """sorted"""
        print(sorted(self))
