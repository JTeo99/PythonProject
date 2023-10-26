import random
import sys
import time

# Initialize the game board size (limit to 80 columns and 24 rows)
max_columns = 80
max_rows = 24
board_size = (min(max_columns, 5), min(max_rows, 5))

# Initialize the player and computer game boards
player_board = [["O" for _ in range(board_size[0])] for _ in range(board_size[1])]
computer_board = [["O" for _ in range(board_size[0])] for _ in range(board_size[1])]

# Initialize the player and computer ship positions
player_ship = [(random.randint(0, board_size[0] - 1), random.randint(0, board_size[1] - 1))]
computer_ship = [(random.randint(0, board_size[0] - 1), random.randint(0, board_size[1] - 1))]


# Function to clear the current line in the terminal
def clear_line():
    sys.stdout.write("\033[K")


# Function to print the game boards with coordinates
def print_boards_with_coordinates(player_board, computer_board):
    # Print column labels
    header = " " * 4  # Initial empty space
    for col in range(board_size[0]):
        header += f"{col:2d} "
    print(header)
    
    for row in range(board_size[1]):
        row_str = f"{row:2d} | "  # Row label
        for col in range(board_size[0]):
            row_str += player_board[row][col] + "  "
        row_str += " | "  # Gap between player and computer boards
        for col in range(board_size[0]):
            row_str += computer_board[row][col] + "  "
        print(row_str)
        print("  | " + " " * (board_size[0] * 3) + " |")

    horizontal_line = "  +-" + "---+" * board_size[0]
    print(horizontal_line)


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
        # Print both game boards with coordinates
        print_boards_with_coordinates(player_board, computer_board)

        # Player's turn
        player_row, player_col = get_user_guess()
        if check_guess(player_row, player_col, computer_ship):
            print("Congratulations! You've sunk the computer's battleship!")
            break
        else:
            if player_board[player_row][player_col] == 'O':
                print("You missed. Try again.")
                player_board[player_row][player_col] = 'X'
            else:
                print("You already guessed this location.")

        time.sleep(1)  # Pause for a moment

        # Clear the previous board display
        for _ in range(board_size[1] * 2 + 5):
            clear_line()
            sys.stdout.write("\033[A")

        # Computer's turn
        computer_row, computer_col = random.randint(0, board_size[0] - 1), random.randint(0, board_size[1] - 1)
        print(f"The computer takes a guess at position: {computer_row} {computer_col}")

        if check_guess(computer_row, computer_col, player_ship):
            print("The computer has sunk your battleship! You lose.")
            break
        else:
            if computer_board[computer_row][computer_col] == 'O':
                print("The computer missed.")
                computer_board[computer_row][computer_col] = 'X'
            else:
                print("The computer already guessed this location.")

        time.sleep(1)  # Pause for a moment

        # Clear the previous board display
        for _ in range(board_size[1] * 2 + 5):
            clear_line()
            sys.stdout.write("\033[A")


# Start the game if this script is run as the main program
if __name__ == "__main__":
    play_battleships()
