#!/usr/bin/python3
"""To check a safe place at a given position"""

import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at a given position.
    """
    """ Check upper diagonal on the left side."""
    for i in range(col):
        if board[row][i] == 1:
            return False

    """
    Check upper diagonal on the left side.
    """
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    """
    Check lower diagonal on the left side.
    """
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, n, solutions):
    if col >= n:
        solutions.append([row[:] for row in board])
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            """ Place the queen """
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, n, solutions)
            board[i][col] = 0


def solve_nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    """ Create an empty chessboard of size n x n """
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be an number")
        sys.exit(1)

    solve_nqueens(N)
