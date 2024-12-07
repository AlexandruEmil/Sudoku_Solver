# Sudoku_Solver

# Description

This project is a Python-based Sudoku Solver that uses the backtracking algorithm to solve puzzles. The solver works with a 9x9 grid, automatically filling in empty cells while following the standard Sudoku rules:

    Each row must contain the digits 1 to 9 without repetition.
    Each column must contain the digits 1 to 9 without repetition.
    Each 3x3 subgrid must contain the digits 1 to 9 without repetition.

# Requirements

    Python 3.x

# Usage 
  ````
  python main.py
  ````

# Features

    Validation: Ensures a number can be placed in a specific position without breaking any Sudoku rules.
    Backtracking Solver: The solver uses the backtracking method, trying different numbers and backtracking when it hits a dead-end.
    Custom Puzzles: You can input your own Sudoku puzzles for the solver to solve.

# Code Structure

    is_valid(board, row, col, num): Checks if a number can be placed in a given position without violating the rules.
    solve_sudoku(board): The main backtracking function that finds the solution to the puzzle.
    board (example puzzle): The initial Sudoku puzzle, where 0 represents empty cells.

# How It Works

The solver tries to place each digit from 1 to 9 in the empty cells and validates if the position is correct. If it finds an invalid position, the solver backtracks and tries a different number. The process continues until the puzzle is completed or no valid solution exists.

>[!NOTE]
>  This project includes unit tests using Python's unittest framework to verify the core functions like ```is_valid()``` and ```solve_sudoku()```. Tests ensure the solver works as expected, including edge cases and various puzzle configurations.

