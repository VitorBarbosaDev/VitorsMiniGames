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


def get_grid_size():
    """Set size of grid"""
    while True:
        try:
            size = int(input("Enter the grid size (e.g., 5 for a 5x5 grid): "))
            if size >= 5:  # Assuming 5 is the minimum acceptable size
                return size
            else:
                print("Please enter a grid size of at least 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def display_grid(grid):
    """Display the grid to the console"""
    for row in grid:
        print(' '.join(row))


def display_guess_grid(grid):
    """Display the grid for guesses to the console"""
    for row in grid:
        print(' '.join(['H' if cell == 'H' else 'M' if cell == 'M' else '~' for cell in row]))


def is_valid_guess(row, col, grid_size):
    """Checks if guess is valid"""
    return 1 <= row <= grid_size and 1 <= col <= grid_size


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


def place_multiple_ships(grid, ship_lengths, placer):
    """Place multiple ships in the grid"""
    for length in ship_lengths:
        if placer == "player":
            place_player_ships(grid, length)
        else:
            place_computer_ships(grid, length)


def is_within_grid(row, col, orientation, length, grid_size):
    """Checks if placement is within grid"""
    if orientation == 'H':
        return col + length <= grid_size
    elif orientation == 'V':
        return row + length <= grid_size
    return False


def is_empty(grid, row, col, orientation, length):
    """Checks if placement is empty"""
    if orientation == 'H':
        return all(grid[row][col + i] == '~' for i in range(length))
    elif orientation == 'V':
        return all(grid[row + i][col] == '~' for i in range(length))
    return False


def is_valid_placement(grid, row, col, orientation, length):
    """Checks if placement is valid"""
    grid_size = len(grid)
    return is_within_grid(row, col, orientation, length, grid_size) and is_empty(grid, row, col, orientation, length)


def place_player_ships(grid, ship_length):
    """Player can enter a place and direction they want their ship to be placed in"""
    while True:
        display_grid(grid)
        try:
            row = int(input(f"Enter the row number to place your {ship_length}-cell ship: "))
            col = int(input("Enter the column number: "))
            orientation = input("Enter the orientation (H for horizontal, V for vertical): ").upper()

            if orientation not in ['H', 'V']:
                print("Invalid orientation. Please enter H or V.")
                continue

            if is_valid_placement(grid, row - 1, col - 1, orientation, ship_length):
                place_ship(grid, row - 1, col - 1, orientation, ship_length)
                break
            else:
                print("Invalid placement. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def place_computer_ships(grid, ship_length):
    """Computer can place a random ship in the grid"""
    while True:
        row = random.randint(0, len(grid) - 1)
        col = random.randint(0, len(grid[0]) - 1)
        orientation = random.choice(['H', 'V'])

        if is_valid_placement(grid, row, col, orientation, ship_length):
            place_ship(grid, row, col, orientation, ship_length)
            break


def make_guess(grid, row, col):
    """Make a guess at the grid"""
    row = row - 1
    col = col - 1
    if grid[row][col] == 'S':
        print("It's a hit!")
        grid[row][col] = 'H'
        return True
    else:
        print("It's a miss!")
        grid[row][col] = 'M'
        return False


def get_player_guess(player_previous_guesses, grid_size):
    """Deals With players Guess"""
    while True:
        try:
            row_input = input("Enter the row number for your guess: \n")
            col_input = input("Enter the column number for your guess: \n")

            if row_input == '' or col_input == '':
                print("You must enter a value for row and column. Try again.")
                continue

            row = int(row_input)
            col = int(col_input)

            if (row, col) in player_previous_guesses:
                print("You've already guessed this location. Try again.")
                continue

            if is_valid_guess(row, col, grid_size):
                return row, col
            else:
                print("Invalid guess. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def computer_turn(player_grid):
    """Deals with computer's turn'"""
    row = random.randint(0, len(player_grid) - 1)
    col = random.randint(0, len(player_grid[0]) - 1)
    return row, col


def main_game_loop(player_grid, computer_grid, ship_lengths):
    """Main game loop"""
    player_ships_sunk = 0
    computer_ships_sunk = 0
    total_ship_cells = sum(ship_lengths)
    player_previous_guesses = set()  # To keep track of player's previous guesses
    grid_size = len(player_grid)

    while player_ships_sunk < total_ship_cells and computer_ships_sunk < total_ship_cells:
        # Player's turn
        print("Your Board:")
        display_grid(player_grid)
        print("Player's Turn:")

        row, col = get_player_guess(player_previous_guesses, grid_size)
        player_previous_guesses.add((row, col))

        if make_guess(computer_grid, row, col):
            player_ships_sunk += 1
        print("Your Guesses:")
        display_guess_grid(computer_grid)

        # Computer's turn
        print("Computer's Turn:")
        row, col = computer_turn(player_grid)

        if make_guess(player_grid, row, col):
            computer_ships_sunk += 1

    if player_ships_sunk == total_ship_cells:
        print("You win!")
    else:
        print("Computer wins!")


# Get grid size from user
grid_size = get_grid_size()

# Initialize a 5x5 grid for player and computer
player_grid = initialize_grid(grid_size)
computer_grid = initialize_grid(grid_size)

# Place multiple ships for player and computer
ship_lengths = [5, 4, 3, 3, 2]

place_multiple_ships(player_grid, ship_lengths, "player")
place_multiple_ships(computer_grid, ship_lengths, "bot")

# Start the main game loop
main_game_loop(player_grid, computer_grid, ship_lengths)
