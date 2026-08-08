#!/usr/bin/python3
"""Module that contains a function that prints a square with #."""


def print_square(size):
    """Prints a square with the character #."""
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
