#!/usr/bin/python3
""" To create a divided matrix """


def matrix_divided(matrix, div):
    """

    Divide all elements of a matrix by a given divisor.

    Args:
    matrix (list of lists): The input matrix, where each row is a list.
    div (int or float): The divisor to all elements by.

    Returns:
    list of lists: A new matrix with elements rounded to 2 decimal places.

    Raises:
    TypeError: If matrix is not a list of lists of integers or floats,
                or if div is not a number (integer or float),
                or if div is equal to 0.
    TypeError: If each row of matrix doesn't have the same size.

    """
    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError("matrix must be a matrix (list of lists) of"
                        "integers/floats")

    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not (isinstance(div, int) or isinstance(div, float)) or div == 0:
        raise TypeError("div must be a number and can't be equal to 0")

    result_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return result_matrix
