#!/usr/bin/python3
"""checks if the obj in the inehrit from class
"""


def is_kind_of_class(obj, a_class):
    """return true if yes and false if not"""
    return True if isinstance(obj, a_class) else False
