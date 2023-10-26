import pygame
import random

# Initialize Pygame
pygame.init()

# Setting constants within the game
# Ensuring tha the maximum screen occupancy of the pygame is within the 
# specified limits
SCREEN_WIDTH, SCREEN_HEIGHT = 80, 24
# Initial set grid size to ensure game works
GRID_SIZE = 5
# Allowing game to take up the whole size of the Pygame Window
CELL_SIZE = SCREEN_WIDTH // GRID_SIZE
# Setting the colours within the game for consistency
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize the game window to specified height and width and sets the title
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Battleships")

# Creating the game board. Uses "O" to represent empty cells in the board
board = [["O" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)

# Place the battleship at a random location within the grid
ship_row = random.randint(0, GRID_SIZE - 1)
ship_col = random.randint(0, GRID_SIZE - 1)