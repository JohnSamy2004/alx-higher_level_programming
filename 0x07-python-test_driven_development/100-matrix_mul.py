#!/usr/bin/python3
"""
This module contains a function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """This function multiplies two matrices
    Args:
        m_a (list of lists of int/float): Matrix to be multiplied
        m_b (list of lists of int/float): Matrix to be multiplied
    Raises:
        TypeError: If m_a or m_b is not a list
        TypeError: If m_a or m_b is not a list of lists
        TypeError: If one element of list of lists is not int/float
        ValueError: If m_a or m_b is empty
        ValueError: If m_a and m_b cannot be multiplied
    Returns:
        A new list which is the outcome of the multiplication
    """

    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or any(not row for row in m_a):
        raise ValueError("m_a can't be empty")
    if m_b == [] or any(not row for row in m_b):
        raise ValueError("m_b can't be empty")

    if any(not isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if any(not isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a):
        raise ValueError("each row of m_a must be of the same size")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise ValueError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    matrix2 = []
    for row_a in m_a:
        my_row = []
        for column_b in zip(*m_b):
            my_row.append(sum(a * b for a, b in zip(row_a, column_b)))
        matrix2.append(my_row)

    return matrix2
