import random
import sys
import time
from tabulate import tabulate


# Function to get user input for the grid size
def get_grid_size():
    while True:
        try:
            size = int(input("Enter the grid size (2-8): "))
            if 2 <= size <= 8:
                return size, size
            else:
                print("Invalid input. Grid size must be between 2 and 8.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


# Initialize the game board size (limit to 80 columns and 24 rows)
max_columns = 80
max_rows = 24
board_size = get_grid_size()

# Initialize the player and computer game boards with labels
player_board = [[" " for _ in range(board_size[1])] for _ in range(board_size[0])]
computer_board = [[" " for _ in range(board_size[1])] for _ in range(board_size[0])]

# Initialize the player and computer ship positions
player_ship = [(random.randint(0, board_size[0] - 1), random.randint(0, board_size[1] - 1))]
computer_ship = [(random.randint(0, board_size[0] - 1), random.randint(0, board_size[1] - 1))]


# Function to clear the current line in the terminal
def clear_line():
    sys.stdout.write("\033[K")


# Function to print the game boards with coordinates and labels
def print_boards_with_coordinates(player_board, computer_board):
    player_board_with_coordinates = [[""] + list(range(1, board_size[1] + 1))] + [[chr(ord('A') + i)] + row for i, row in enumerate(player_board)]
    computer_board_with_coordinates = [[""] + list(range(1, board_size[1] + 1))] + [[chr(ord('A') + i)] + row for i, row in enumerate(computer_board)]

    print("Player's Grid:")
    print(tabulate(player_board_with_coordinates, tablefmt="grid"))
    print("\nComputer's Grid:")
    print(tabulate(computer_board_with_coordinates, tablefmt="grid"))


# Function to get the user's guess (row and column)
def get_user_guess():
    while True:
        try:
            guess = input(f"Enter your guess (rowcolumn, max {chr(ord('A') + board_size[0] - 1)}{board_size[1]}): ")
            col_row = guess.upper()
            col = ord(col_row[0]) - ord('A')  # Convert column letter to zero-based index
            row = int(col_row[1:]) - 1  # Subtract 1 to convert from 1-based to 0-based index
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
    print("Welcome to Battleships!")

    while True:
        # Print both game boards with coordinates and labels
        print_boards_with_coordinates(player_board, computer_board)

        # Player's turn
        player_row, player_col = get_user_guess()
        if check_guess(player_row, player_col, computer_ship):
            print("Congratulations! You've sunk the computer's battleship!")
            break
        else:
            if player_board[player_row][player_col] == ' ':
                print("You missed. Try again.")
                player_board[player_row][player_col] = 'X'
            else:
                print("You already guessed this location.")

        time.sleep(1)  # Pause for a moment

        # Clear the previous board display
        for _ in range(board_size[0] + 5):
            clear_line()
            sys.stdout.write("\033[A")

        # Computer's turn
        computer_row, computer_col = random.randint(0, board_size[0] - 1), random.randint(0, board_size[1] - 1)
        print(f"The computer takes a guess at position: {chr(ord('A') + computer_row)} {computer_col + 1}")

        if check_guess(computer_row, computer_col, player_ship):
            print("The computer has sunk your battleship! You lose.")
            break
        else:
            if computer_board[computer_row][computer_col] == ' ':
                print("The computer missed.")
                computer_board[computer_row][computer_col] = 'X'
            else:
                print("The computer already guessed this location.")

    time.sleep(1)  # Pause for a moment

    # Calculate the number of rows needed to clear the screen
    rows_to_clear = (board_size[0] + 5) * 2  # Includes player's grid, headers, and computer's grid

    # Clear the screen by using sys and printing newline characters
    for _ in range(rows_to_clear):
        sys.stdout.write("\033[K\n")


# Start the game if this script is run as the main program
if __name__ == "__main__":
    play_battleships()
