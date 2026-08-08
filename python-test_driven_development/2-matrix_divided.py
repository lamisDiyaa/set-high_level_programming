#!/usr/bin/python3
"""Module that contains a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div, rounded to 2 decimal places."""
    type_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(type_msg)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(type_msg)
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError(type_msg)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
