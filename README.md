# 🔢 Sudoku Solver

This project allows users to input their own 9x9 Sudoku grid or retrieve a random puzzle from the Dosuku API. The algorithm uses recursive backtracking to solve the puzzle, ensuring the validity of the solution by checking rows, columns, and 3x3 subgrids.

# 🚀 Features
- ✅ Allows users to input a custom Sudoku puzzle or fetch a random one
- ✅ Implements recursive backtracking to efficiently solve Sudoku puzzles
- ✅ Validates the puzzle by checking for duplicates in rows, columns, and 3x3 subgrids
- ✅ Prints the solved grid or notifies if no solution is possible


# 📈 How It Works
1️⃣ Sudoku Validation: Checks if there are any duplicate numbers in rows, columns, or 3x3 subgrids.

2️⃣ Recursive Backtracking: Tries all possible values for empty cells, backtracking if an invalid move is made.

3️⃣ Fetches Random Sudoku: If the user opts for a random puzzle, the program pulls it from the Dosuku API.

