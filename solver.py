# function that checks if the given matrix is a valid sudoku or not
# if freq of number is > 1 then return false, else return true

import numpy as np

class Solution(object):
    def __init__(self, grid):
        """
        Initializing funtion for Solution class
        """
        self.grid = grid
        self.options = list(range(1,10)) # Options to input in gridg
    
    def valid_idx(self, row_idx, col_idx, num):
        """
        Takes in a specific cell index and number to check if grid forms a valid sudoku:
            - Checks if the row index has any number duplicates
            - Checks if the column index has any number duplicates
            - Checks if the relevant 3x3 square has any number duplicates
        """
        # Set value for that row and col to the given number
        self.grid[row_idx, col_idx] = num

        # Extract relevant row and column from grid
        row = self.grid[row_idx]
        col = self.grid[:,col_idx]

        # Extract relevant 3x3 square from grid
        sq_rmin = 3*(row_idx // 3)
        sq_cmin = 3*(col_idx // 3)
        sq = self.grid[sq_rmin : sq_rmin + 3, sq_cmin : sq_cmin + 3]

        # Check if any number has frequency greater than 1
        for i in range(1,10):
            row_count = (row == i).sum()
            col_count = (col == i).sum()
            sq_count = (sq == i).sum()

            if row_count > 1 or col_count > 1 or sq_count > 1:
                return False
        
        # If all count <= 1, then grid is valid
        return True
    
    def solve_sudoku(self):
        """
        Recursive function that 
        """
        # Runs through each element of grid
        for i in range(9):
            for j in range(9):

                # Checks if grid is unfilled
                if self.grid[i,j] == 0:
                    
                    # Runs through possible number possibilities
                    for k in self.options:
                        
                        # If the cell index and number form a valid sudoku, run recursive function after setting that cell index as that number
                        if self.valid_idx(i, j, k):
                            self.grid[i,j] = k
                            if self.solve_sudoku():
                                return True
                            # If recursive function returns False, then reset cell index as 0
                            self.grid[i,j] = 0
                        
                        # If the cell index and number do not form a valid sudoku, ensure current cell is 0
                        self.grid[i,j] = 0
                    
                    # If there are no valid number possibilities, sudoku is not valid
                    return False
        
        # This only returns true if the sudoku is valid
        return True