#!/usr/bin/python3
"""Module that contains a function that multiplies 2 matrices using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices by using NumPy."""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    row_len_a = len(m_a[0])
    if not all(len(row) == row_len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    row_len_b = len(m_b[0])
    if not all(len(row) == row_len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    return np.matmul(m_a, m_b)
