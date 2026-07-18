#!/usr/bin/python3
"""This module defines a class Square."""


class Square:
    """A class that defines a square."""
    def __init__(self, size=0):
        """Initializes the square."""
        self.size = size

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size with validation for int or float."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Compares if equal."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compares if not equal."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Compares if less than."""
        return self.area() < other.area()

    def __le__(self, other):
        """Compares if less than or equal."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compares if greater than."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compares if greater than or equal."""
        return self.area() >= other.area()
