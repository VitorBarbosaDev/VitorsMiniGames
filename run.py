# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def initialize_grid(size):
    """
    Create a grid of size 'size x size' filled with '~'
    ~ represents empty water
    """
    grid = [['~' for _ in range(size)] for _ in range(size)]
    return grid

def display_grid(grid):
    # Display the grid to the console
    for row in grid:
        print(' '.join(row))


# Initialize a 5x5 grid
grid_size = 5
grid = initialize_grid(grid_size)

# Display the initial grid
display_grid(grid)