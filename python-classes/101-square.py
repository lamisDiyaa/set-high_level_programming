#!/usr/bin/python3
"""This module defines a class Square."""


class Square:
    """A class that defines a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current area."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with #."""
        if self.__size == 0:
            print("")
            return
        [print("") for _ in range(self.__position[1])]
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Defines the printable representation of a Square instance."""
        res = []
        if self.__size == 0:
            return ""
        [res.append("") for _ in range(self.__position[1])]
        for _ in range(self.__size):
            res.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(res)
