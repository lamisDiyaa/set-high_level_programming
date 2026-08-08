#!/usr/bin/python3
"""Module that contains the Base class."""


class Base:
    """Base class for managing id attributes across the project."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
