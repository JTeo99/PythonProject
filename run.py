import random

# Initialize the game board
board_size = 5
board = [["O" for _ in range(board_size)] for _ in range(board_size)]

# Initialize the player and computer ship positions
player_ship = [(random.randint(0, board_size - 1), random.randint(0, board_size - 1))]
computer_ship = [(random.randint(0, board_size - 1), random.randint(0, board_size - 1))]