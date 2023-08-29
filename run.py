# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

"""
~ for empty (water)
S for a ship
H for a hit
M for a miss
"""

import random

def initialize_grid(size):
    """
    Create a grid of size 'size x size' filled with '~'
    ~ represents empty water
    """
    grid = [['~' for _ in range(size)] for _ in range(size)]
    return grid

def display_grid(grid):
    """Display the grid to the console"""
    for row in grid:
        print(' '.join(row))






def place_ship(grid, row, col, orientation, length):
    """
    Place a ship of length 'length' in the grid at row 'row' and column 'col'
    """
    if orientation == 'H':
        for i in range(length):
            grid[row][col + i] = 'S'
    elif orientation == 'V':
        for i in range(length):
            grid[row + i][col] = 'S'

def place_player_ships(grid, ship_length):
    display_grid(player_grid)
    row = int(input("Enter the row number to place your ship: "))
    col = int(input("Enter the column number to place your ship: "))
    orientation = input("Enter the orientation (H for horizontal, V for vertical): ")
    place_ship(grid, row, col, orientation, ship_length)

# Initialize a 5x5 grid for player and computer
player_grid = initialize_grid(5)
computer_grid = initialize_grid(5)



# Place a 3-cell long ship for player
place_player_ships(player_grid, 3)


# Display the grids
print("Player Grid:")
display_grid(player_grid)