import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
# Ensuring tha the maximum screen occupancy of the pygame is within the
# specified limits
WIDTH, HEIGHT = 400, 400
# Initial set grid size to ensure game works
GRID_SIZE = 5
# Allowing game to take up the whole size of the Pygame Window
CELL_SIZE = WIDTH // GRID_SIZE
# Setting the colours within the game for consistency
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize the game window to specified height and width and sets the title
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battleship Game")

# # Creating the game board. Uses "O" to represent empty cells in the board
board = [["O" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Place the battleship at a random location
ship_row = random.randint(0, GRID_SIZE - 1)
ship_col = random.randint(0, GRID_SIZE - 1)

# Game loop - game runs as long as running is true
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Obtains position of mouse click to work out corresponding grid space
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            guess_row = y // CELL_SIZE
            guess_col = x // CELL_SIZE

            # Check if the guess is valid
            if board[guess_row][guess_col] == "X":
                continue

            # Check if the guess is a hit or miss
            if guess_row == ship_row and guess_col == ship_col:
                board[guess_row][guess_col] = "X"
                print("Congratulations! You sunk my battleship!")
            else:
                board[guess_row][guess_col] = "X"

    screen.fill(WHITE)

    # Draw the game board including hit and grid lines
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect_x = col * CELL_SIZE
            rect_y = row * CELL_SIZE
            rect_width = CELL_SIZE
            rect_height = CELL_SIZE
            pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height), 1)
            
            if board[row][col] == "X":
                circle_x = col * CELL_SIZE + CELL_SIZE // 2
                circle_y = row * CELL_SIZE + CELL_SIZE // 2
                circle_radius = CELL_SIZE // 2 - 2
                pygame.draw.circle(screen, RED, (circle_x, circle_y), circle_radius)
    
    # Updating the display for the current game board
    pygame.display.update()

    # Check for game over
    if all(cell == "X" for row in board for cell in row):
        print("Game Over")
        print(f"The battleship was at Row {ship_row + 1}, Col {ship_col + 1}.")
        break

pygame.quit()
