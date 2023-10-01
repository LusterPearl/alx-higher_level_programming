#!/usr/bin/python3

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using Numpy

    Args:
        m_a (list of lists): The first matrix represented as a list of lists.
        m_b (list of lists): The second matrix represented as a list of lists.


    Returns:
        list of lists: The result of the matrix multiplicstion as a list of lists.
    """
    return (np.matmul(m_a, m_b))
