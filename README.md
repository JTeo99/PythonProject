# Battleships Game

This is a command-line implementation of the classic Battleships game. The game features a player grid and a computer grid, and players take turns guessing the locations of each other's ships.

## Dependencies

- `tabulate`: A Python library for formatting tables in the console.
- `colorama`: A library for adding colored output to the terminal.

## Game Functions

### `clear_terminal()`

- Clears the terminal screen to remove previous instances of the game.

### `get_grid_size()`

- Obtains the user's input for the grid size, ensuring that the number of rows and columns is between 2 and 6.

### `reset_board(board_size)`

- Initializes the player and computer game boards with empty cells.

### `print_message(message, color=RESET)`

- Prints messages in color to the terminal.

### `clear_line()`

- Clears the current line in the terminal.

### `generate_coordinates(board, board_size)`

- Generates the game board with coordinates and labels, including row numbers and column letters.

### `print_coordinates(player_board, comp_board, board_size)`

- Prints both game boards with coordinates and labels, creating a visual representation of the game grids.

### `get_user_guess(board_size)`

- Gets the user's guess for a cell, ensuring correct input format and valid coordinates.
- Supports the "restart" command to clear the terminal and restart the game.
- Converts user input to uppercase for uniformity.

### `check_guess(row, col, target_ship)`

- Checks if a guess hits a ship by comparing the input row and column to a target ship's positions.

### `play_battleships()`

- The main game loop function that manages the game logic.
- Alternates between player and computer turns, checking for hits.
- Notifies the player of their success or failure.
- Provides the option to play the game again.

## Running the Game

- Run this script as the main program to start the Battleships game.

Have fun playing Battleships!