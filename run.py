import random

# Initialize the game board size (limit to 80 columns and 24 rows)
max_columns = 80
max_rows = 24
board_size = (min(max_columns, 5), min(max_rows, 5))

# Initialize the game board
board = [["O" for _ in range(board_size[0])] for _ in range(board_size[1])]

# Initialize the player and computer ship positions
player_ship = [(random.randint(0, board_size[0] - 1), random.randint(0, board_size[1] - 1))]
computer_ship = [(random.randint(0, board_size[0] - 1), random.randint(0, board_size[1] - 1)]

# Function to print the game board
def print_board(board):
    for row in board:
        print(" ".join(row))

# Function to get the user's guess (row and column)
def get_user_guess():
    while True:
        try:
            guess = input("Enter your guess (row and column): ")
            row, col = map(int, guess.split())
            if 0 <= row < board_size and 0 <= col < board_size:
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
    print_board(board)
    
    while True:
        # Player's turn
        player_row, player_col = get_user_guess()
        if check_guess(player_row, player_col, computer_ship):
            print("Congratulations! You've sunk the computer's battleship!")
            break
        else:
            print("You missed. Try again.")
            board[player_row][player_col] = "X"
        
        # Computer's turn
        computer_row, computer_col = random.randint(0, board_size - 1), random.randint(0, board_size - 1)
        print("The computer takes a guess at position: {} {}".format(computer_row, computer_col))
        
        if check_guess(computer_row, computer_col, player_ship):
            print("The computer has sunk your battleship! You lose.")
            break
        else:
            print("The computer missed.")
            board[computer_row][computer_col] = "X"
        
        print_board(board)

# Start the game if this script is run as the main program
if __name__ == "__main__":
    play_battleships()