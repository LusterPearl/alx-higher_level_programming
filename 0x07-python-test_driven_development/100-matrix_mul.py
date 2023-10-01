#!/usr/bin/python3
"""Module to perform matrix multiplication."""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices m_a and m_b.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        list of lists: The result of matrix multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list, or contains non-int/floats.
        ValueError: If m_a or m_b is empty  or can't be multiplied.

    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list amd m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) \
            or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists and m_b must "
                        "be a list of lists")

    if not m_a or not m_b:
        raise ValueError("m_a can't be empty and m_b can't be empty")

    for row in m_a:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(len(row) == len(m_a[0]) for row in m_a) \
                or not all(len(row) == len(m_b[0]) for row in m_b):
            raise ValueError("each row if m_a must be of the same size "
                             "and each row of m_b must be of the same size")

        if len(m_a[0]) != len(m_b):
            raise ValueError("m_a and m_b can't be multiplied")

        result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
        for i in range(len(m_a)):
            for j in range(len(m_b[0])):
                for k in range(len(m_b)):
                    result[i][j] += m_a[i][k] * m_b[k][j]

        return result
