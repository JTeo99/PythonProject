import pygame
import random

# Initialize Pygame
pygame.init()

# Setting constants within the game
# Ensuring tha the maximum screen occupancy of the pygame is within the specified limits
SCREEN_WIDTH, SCREEN_HEIGHT = 80, 24
# Initial set grid size to ensure game works
GRID_SIZE = 5
# Allowing game to take up the whole size of the Pygame Window
CELL_SIZE = SCREEN_WIDTH // GRID_SIZE
# Setting the colours within the game for consistency
WHITE = (255, 255, 255)
RED = (255, 0, 0)