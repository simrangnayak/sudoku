import requests
import numpy as np
from solver import Solution
from ast import literal_eval

def run():
    """
    This asks the user whether they want to input their own sudoku or get a random sudoku. In the case of the latter, this code uses data from Dosuku to grab a randomnly generated sudoku. If the user opts to use their own sudoku, they must input a 9x9 grid using nested grids.

    If there is a solution, the code prints the solved 9x9 grid. If not, the code prints there is no solution possible.
    """
    # Ask if player would like to provide their own sudoku
    player = input("Would you like to provide your own sudoku? (y/n): ")

    if player.lower() != 'y' and player.lower() != 'n':
        raise ValueError('Not entered valid input.')
    
    # If yes, ask player to enter 
    if player.lower() == 'y':
        response = input("Please provide a 9x9 sudoku grid, in nested list format (let unfilled cells have 0): ")
        grid = literal_eval(response) # Turns str representation into grid
    
    # If no, extract sudoku from dosuku website
    else:
        url = 'https://sudoku-api.vercel.app/api/dosuku?query={newboard(limit:1){grids{value}}}'
        response = literal_eval(requests.get(url).text)
        sudoku = response["newboard"]["grids"][0] # Parsing dictionary output from random sudoku generator
        grid = sudoku["value"]
    
    # Print sudoku problem
    np_grid = np.array(grid)
    print("Sudoku Problem:")
    print(np_grid)
    print("\n")

    # Run and print solution
    solution = Solution(np_grid)
    if solution.solve_sudoku():
        print("Solution:")
        print(solution.grid)
    else:
        print("No solution possible.")

if __name__ == '__main__':
    run()