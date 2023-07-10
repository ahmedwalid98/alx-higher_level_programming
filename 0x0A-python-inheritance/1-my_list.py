#!/usr/bin/python3
"""class MyList inherit from list
"""

class MyList(list):
    """
    args: list
    methods: print sorted
    """
    def print_sorted(self):
        """print list"""
        print(sorted(self))
