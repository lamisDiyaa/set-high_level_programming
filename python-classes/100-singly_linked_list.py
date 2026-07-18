#!/usr/bin/python3
"""This module defines nodes and a singly linked list."""


class Node:
    """Defines a node of a singly linked list."""
    def __init__(self, data, next_node=None):
        """Initializes a Node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets data with type validation."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node with validation."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""
    def __init__(self):
        """Initializes the list."""
        self.__head = None

    def __str__(self):
        """Makes the list printable, one number per line."""
        values = []
        current = self.__head
        while current:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """Inserts a new Node in the correct sorted position."""
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node
