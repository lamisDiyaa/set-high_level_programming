#!/usr/bin/python3
"""Module that contains a function that appends a string to a text file."""


def append_write(filename="", text=""):
    """Appends a string at the end of a UTF8 text file and returns added chars."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
