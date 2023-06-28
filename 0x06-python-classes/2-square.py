#!/usr/bin/python3
"""Define a class called Square."""


class Square:
    """make a square class"""

    def __init__(self, size=0):
        """define a square

        Args:
            size (int): The size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
