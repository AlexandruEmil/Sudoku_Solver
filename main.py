from sudoku import SudokuSolver

if __name__ == "__main__":
    puzzles = [
    # Sudoku 1
    [
      [5, 3, 0, 0, 7, 0, 0, 0, 0],
      [6, 0, 0, 1, 9, 5, 0, 0, 0],
      [0, 9, 8, 0, 0, 0, 0, 6, 0],
      [8, 0, 0, 0, 6, 0, 0, 0, 3],
      [4, 0, 0, 8, 0, 3, 0, 0, 1],
      [7, 0, 0, 0, 2, 0, 0, 0, 6],
      [0, 6, 0, 0, 0, 0, 2, 8, 0],
      [0, 0, 0, 4, 1, 9, 0, 0, 5],
      [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ],
    # Sudoku 2 
    [
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ],
    # Sudoku 3
    [
      [0, 5, 0, 0, 2, 0, 0, 0, 0],
      [2, 0, 0, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 9, 6],
      [0, 0, 0, 0, 1, 0, 0, 4, 9],
      [0, 3, 2, 0, 0, 0, 5, 8, 0],
      [6, 9, 0, 0, 7, 0, 0, 0, 0],
      [9, 4, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 2, 0, 0, 0, 0, 8],
      [0, 0, 0, 0, 8, 0, 0, 3, 0]
    ],
    # Sudoku 4 
    [
      [0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 4, 0, 0],
      [8, 7, 0, 0, 0, 3, 0, 0, 0],
      [0, 0, 2, 0, 0, 7, 0, 0, 0],
      [0, 0, 0, 0, 0, 8, 0, 4, 0],
      [0, 1, 0, 0, 0, 0, 6, 0, 0],
      [0, 2, 0, 5, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 0, 3, 0, 0, 0, 0, 0]
    ],
    # Sudoku 5 
    [
      [0, 0, 7, 0, 9, 0, 0, 0, 2],
      [0, 0, 0, 6, 0, 3, 0, 7, 0],
      [3, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 8, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 2, 0, 0, 0, 0, 0],
      [0, 0, 9, 0, 0, 0, 0, 6, 0],
      [4, 0, 0, 3, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 4, 0, 0, 7],
      [7, 0, 0, 0, 0, 0, 3, 0, 0]
    ],
    # sudoku 6
    [
    [5, 0, 0, 0, 3, 0, 0, 8, 0],
    [0, 0, 6, 0, 0, 0, 1, 0, 0],
    [0, 7, 0, 5, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 9, 0, 0, 3, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 6],
    [0, 5, 0, 0, 2, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 7, 0, 4, 0],
    [0, 0, 8, 0, 0, 0, 5, 0, 0],
    [0, 2, 0, 0, 6, 0, 0, 0, 3]
    ]
    ]

    for i, puzzle in enumerate(puzzles, start=1):
        solver = SudokuSolver(puzzle)
        
        print(f"Solving Sudoku {i}:")
        if solver.solve():
            solution = solver.get_solution()
            for row in solution:
                print(" ".join(map(str, row)))
            print("\nSolution found!\n")
        else:
            print("No solution exists for this Sudoku.\n")