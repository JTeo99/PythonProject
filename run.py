import random
import sys
import time
from tabulate import tabulate
import os

# ANSI color codes
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[H")


# Function to get user input for the grid size
def get_grid_size():
    while True:
        try:
            rows = int(input("Enter the number of rows (2-6): "))
            columns = int(input("Enter the number of columns (2-6): "))
            if 2 <= rows <= 6 and 2 <= columns <= 6:
                return rows, columns
            else:
                print("Invalid input. Rows and columns must be between 2 and 6.")
        except ValueError:
            print("Invalid input. Please enter valid integers.")


# Initialize the game board size (limit to 80 columns and 24 rows)
max_columns = 80
max_rows = 24
board_size = get_grid_size()

# Initialize the player and computer game boards with labels
player_board = [[" " for _ in range(board_size[1])]
                for _ in range(board_size[0])]
computer_board = [[" " for _ in range(board_size[1])]
                  for _ in range(board_size[0])]

# Initialize the player and computer ship positions
player_ship = [(random.randint(0, board_size[0] - 1),
                random.randint(0, board_size[1] - 1))]
computer_ship = [(random.randint(0, board_size[0] - 1),
                  random.randint(0, board_size[1] - 1))]


# Function to print messages in color
def print_message(message, color=RESET):
    print(color + message + RESET)


# Function to clear the current line in the terminal
def clear_line():
    sys.stdout.write("\033[K")


# Function to generate the board with coordinates and labels
def generate_board_with_coordinates(board):
    header = [""]
    header += [chr(ord('A') + i) for i in range(board_size[1])]
    header += [""]
    result = [header]

    for i, row in enumerate(board):
        result.append([str(i + 1)] + row + [str(i + 1)])
    result.append(header)
    return result


# Function to print the game boards with coordinates and labels
def print_boards_with_coordinates(player_board, computer_board):
    clear_terminal()
    player_board_with_coordinates = generate_board_with_coordinates(player_board)
    computer_board_with_coordinates = generate_board_with_coordinates(computer_board)

    print("Player's Grid:")
    print(tabulate(player_board_with_coordinates, tablefmt="grid"))

    # Add a gap between player and computer grids
    print("\n" + " " * 6 + "+--" + "--+" * board_size[1] + "\n")

    print("Computer's Grid:")
    print(tabulate(computer_board_with_coordinates, tablefmt="grid"))


# Function to get the user's guess (row and column)
def get_user_guess():
    while True:
        try:
            guess = input(f"Enter your guess (e.g., A1, max {chr(ord('A') + board_size[1] - 1)}{board_size[0]}): ")
            col_row = guess.upper()
            # Convert column letter to zero-based index
            col = ord(col_row[0]) - ord('A')
            # Subtract 1 to convert from 1-based to 0-based index
            row = int(col_row[1:]) - 1
            if 0 <= col < board_size[1] and 0 <= row < board_size[0]:
                return row, col
            else:
                print("Invalid input. Please enter valid row and column values.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid row and column values.")


# Function to check if a guess hits a ship
def check_guess(row, col, target_ship):
    if (row, col) in target_ship:
        return True
    return False


# Main game loop
def play_battleships():
    print_message("Welcome to Battleships!", GREEN)

    while True:
        clear_terminal()
        # Print both game boards with coordinates and labels
        print_boards_with_coordinates(player_board, computer_board)

        # Player's turn
        player_row, player_col = get_user_guess()
        if check_guess(player_row, player_col, computer_ship):
            print_message("Congratulations! You've sunk the computer's battleship!", GREEN)
            break
        else:
            if player_board[player_row][player_col] == ' ':
                print_message("You missed. Try again.", RED)
                player_board[player_row][player_col] = 'X'
            else:
                print_message("You already guessed this location.", RED)

        time.sleep(1)  # Pause for a moment

        # Clear the previous board display
        for _ in range(board_size[0] + 5):
            clear_line()
            sys.stdout.write("\033[A")

        # Computer's turn
        computer_row, computer_col = random.randint(0, board_size[0] - 1), random.randint(0, board_size[1] - 1)
        print_message(f"The computer takes a guess at position: {chr(ord('A') + computer_row)} {computer_col + 1}", GREEN)

        if check_guess(computer_row, computer_col, player_ship):
            print_message("The computer has sunk your battleship! You lose.", RED)
            break
        else:
            if computer_board[computer_row][computer_col] == ' ':
                print_message("The computer missed.", RED)
                computer_board[computer_row][computer_col] = 'X'
            else:
                print_message("The computer already guessed this location.", RED)

    time.sleep(1)  # Pause for a moment


# Start the game if this script is run as the main program
if __name__ == "__main__":
    play_battleships()
