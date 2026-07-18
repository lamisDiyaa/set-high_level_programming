#!/usr/bin/python3
"""N Queens puzzle solver module."""
import sys


def init_board(n):
    """Initializes an empty list for solutions."""
    return []


def is_safe(board, row, col):
    """Checks if a queen can be placed at board[row] = col."""
    for r, c in board:
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


def solve_nqueens(n, row, board):
    """Uses backtracking to find all solutions."""
    if row == n:
        print(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board.append([row, col])
            solve_nqueens(n, row + 1, board)
            board.pop()


def main():
    """Main entry point for the execution."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(n)
    solve_nqueens(n, 0, board)


if __name__ == "__main__":
    main()
