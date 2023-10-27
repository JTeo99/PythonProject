from tabulate import tabulate
from colorama import Fore, Back, Style, init

import random
import sys
import time
import os

init(autoreset=True)  # Initializing Colorama

GREEN = Fore.GREEN
RED = Fore.RED
RESET = Style.RESET_ALL


def clear_terminal():
    """
    Function to get user input for the grid size. Prompts the user for the
    number of rows and columns, ensuring they are between 2 and 6.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[H")


def get_grid_size():  # Function to get user input for the grid size
    """
    Function to get user input for the grid size. Prompts the user for the
    number of rows and columns, ensuring they are between 2 and 6.
    """
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


def reset_board(board_size):
    """
    Initialize the game boards
    """
    player_board = [[" " for _ in range(board_size[1])]
                    for _ in range(board_size[0])]
    comp_board = [[" " for _ in range(board_size[1])]
                  for _ in range(board_size[0])]
    return player_board, comp_board


def print_message(message, color=RESET):  # Function to print messages in color
    print(color + message + RESET)


def clear_line():  # Function to clear the current line in the terminal
    sys.stdout.write("\033[K")


def generate_coordinates(board, board_size):
    """
    Function to generate the game board with coordinates and labels. The
    coordinates include row numbers and column letters. This function
    creates the top row labels.
    """
    header = [""]
    header += [chr(ord('A') + i) for i in range(board_size[1])]
    header += [""]
    result = [header]

    # Generating rows with data and row labels
    for i, row in enumerate(board):
        result.append([str(i + 1)] + row + [str(i + 1)])
    return result


def print_coordinates(player_board, comp_board, board_size):
    """
    Function to print both game boards with coordinates and labels. It creates
    the visual representation of the game boards and their labels.
    """
    player_coordinates = generate_coordinates(player_board, board_size)
    comp_coordinates = generate_coordinates(comp_board, board_size)

    """
    Prints labels for the Player's side of the grid and Computer's side of the
    grid. Initializes an empty list to later store the combined grid for the
    player and the computer.
    """

    # Print labels above the table
    print("Player's Grid" + "    " * board_size[1] + "Computer's Grid")

    combined_grid = []

    # Combine player and computer grid rows for display
    for i in range(max(len(player_coordinates), len(comp_coordinates))):
        player_row = player_coordinates[i] if i < len(player_coordinates) else [""] * (board_size[1] + 2)
        comp_row = comp_coordinates[i] if i < len(comp_coordinates) else [""] * (board_size[1] + 2)
        combined_row = player_row + comp_row
        combined_grid.append(combined_row)

    print(tabulate(combined_grid, tablefmt="grid"))


def get_user_guess(board_size):
    """
    Function to get the user's guess (row and column). It ensures that the
    user's input is correctly formatted and within the game's bounds.
    """
    while True:
        try:
            guess = input(f"Enter your guess (e.g., A1, max {chr(ord('A') + board_size[1] - 1)}{board_size[0]}): ")

            if (guess == "restart"):
                """
                checks for "restart" as an input to stop the rest of the game
                and clear the terminal. Time library for 1 second
                break before 'calling play-battleships()' to rebuild the game.
                """
                clear_terminal()
                time.sleep(1)
                play_battleships()

            """
            Converts stored guess to upper case
            """
            col_row = guess.upper()

            # Column letter to zero-based index
            col = ord(col_row[0]) - ord('A')

            # Subtract 1 to convert from 1-based to 0-based index
            row = int(col_row[1:]) - 1

            if 0 <= col < board_size[1] and 0 <= row < board_size[0]:

                clear_terminal()
                time.sleep(1)
                return row, col

            else:
                print("Invalid input. Please enter valid row and column values.")

        except (ValueError, IndexError):
            print("Invalid input. Please enter valid row and column values.")


def check_guess(row, col, target_ship):
    """
    Function to check if a guess hits a ship. It checks if the provided row
    and column match any of the positions in the target ship.
    """
    if (row, col) in target_ship:
        return True
    return False


def play_battleships():
    """
    Main game loop function. It manages the game logic, including player and
    computer turns, checking for hits, and asking if the player wants to
    play again.
    """
    while True:

        board_size = get_grid_size()  # setting board size

        player_board, comp_board = reset_board(board_size)  # reset board

        print_message("Welcome to Battleships!", GREEN)

        while True:
            # Print both game boards with coordinates and labels
            print_coordinates(player_board, comp_board, board_size)
            player_ship = [(random.randint(0, board_size[0] - 1),
                            random.randint(0, board_size[1] - 1))]
            comp_ship = [(random.randint(0, board_size[0] - 1),
                          random.randint(0, board_size[1] - 1))]

            # Player's turn
            player_row, player_col = get_user_guess(board_size)

            if check_guess(player_row, player_col, comp_ship):
                print_message("Wow! You've sunk the enemy battleship!", GREEN)
                break

            elif (player_board[player_row][player_col] == ' '):
                print_message("You missed. Try again.", RED)
                player_board[player_row][player_col] = 'X'

            else:
                print_message("You already guess here.", RED)

            # Clear the previous board display
            for _ in range(board_size[0] + 5):
                clear_line()
                sys.stdout.write("\033[A")

            '''
            Computer's turn to pick. Randomely selects a set of coordinates
            within the range of the grid and prints the location by which the
            computer chose. Player loses if Computer guesses correctly but
            loops to player pick if computer is incorrect.
            '''
            comp_row, comp_col = random.randint(0, board_size[0] - 1), random.randint(0, board_size[1] - 1)
            print_message(f"The computer takes a guess at position: {chr(ord('A') + comp_row)} {comp_col + 1}", GREEN)

            if check_guess(comp_row, comp_col, player_ship):
                print_message("Your battleship has sunk! You lose.", RED)
                break

            elif (comp_board[comp_row][comp_col] == ' '):
                print_message("The computer missed.", RED)
                comp_board[comp_row][comp_col] = 'X'

            else:
                print_message("The computer already guessed here.", RED)
        """
        restart built into the game
        """
        restart = input("Do you want to play again? (yes/no): ").strip().lower()
        if restart != 'yes':
            break


# Start the game if this script is run as the main program
if __name__ == "__main__":
    play_battleships()
