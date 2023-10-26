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
player_board = [[" " for _ in range(board_size[0] + 1)] for _ in range(board_size[1] + 1)]
computer_board = [[" " for _ in range(board_size[0] + 1)] for _ in range(board_size[1] + 1)]

# Initialize the player and computer ship positions
player_ship = [(random.randint(0, board_size[0] - 1), random.randint(0, board_size[1] - 1))]
computer_ship = [(random.randint(0, board_size[0] - 1), random.randint(0, board_size[1] - 1))]


# Function to clear the current line in the terminal
def clear_line():
    sys.stdout.write("\033[K")


# Function to print the game boards with coordinates and labels
def print_boards_with_coordinates(player_board, computer_board):
    headers = [list(range(board_size[0] + 1)), list(range(board_size[0] + 1))]
    headers[0][0] = " "
    headers[1][0] = " "
    headers[0][1] = "|"
    headers[1][1] = "|"

    player_board[0][1:] = headers[0][2:]
    computer_board[0][1:] = headers[0][2:]
    player_board[1][1:] = headers[1][2:]
    computer_board[1][1:] = headers[1][2:]

    player_table = tabulate(player_board, headers, tablefmt="grid")
    computer_table = tabulate(computer_board, headers, tablefmt="grid")

    print("Player's Grid:")
    print(player_table)
    print()
    print("Computer's Grid:")
    print(computer_table)


# Function to get the user's guess (row and column)
def get_user_guess():
    while True:
        try:
            guess = input(f"Enter your guess (row and column, max {board_size[0] - 1} {board_size[1] - 1}): ")
            row, col = map(int, guess.split())
            if 0 <= row < board_size[0] and 0 <= col < board_size[1]:
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
            if player_board[player_row + 2][player_col + 2] == ' ':
                print("You missed. Try again.")
                player_board[player_row + 2][player_col + 2] = 'X'
            else:
                print("You already guessed this location.")

        time.sleep(1)  # Pause for a moment

        # Clear the previous board display
        for _ in range(board_size[1] * 4 + 7):
            clear_line()
            sys.stdout.write("\033[A")

        # Computer's turn
        computer_row, computer_col = random.randint(0, board_size[0] - 1), random.randint(0, board_size[1] - 1)
        print(f"The computer takes a guess at position: {computer_row} {computer_col}")

        if check_guess(computer_row, computer_col, player_ship):
            print("The computer has sunk your battleship! You lose.")
            break
        else:
            if computer_board[computer_row + 2][computer_col + 2] == ' ':
                print("The computer missed.")
                computer_board[computer_row + 2][computer_col + 2] = 'X'
            else:
                print("The computer already guessed this location.")

        time.sleep(1)  # Pause for a moment

        # Clear the previous board display
        for _ in range(board_size[1] * 4 + 7):
            clear_line()
            sys.stdout.write("\033[A")


# Start the game if this script is run as the main program
if __name__ == "__main__":
    play_battleships()
