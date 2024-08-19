# Turtle XOX Game

## Overview

The Turtle XOX game is a classic Tic-Tac-Toe game implemented using Python's Turtle Graphics module. This game allows two players to take turns placing "X" or "O" on a 3x3 grid, aiming to get three of their symbols in a row to win.

## Features

- Interactive 3x3 grid for gameplay.
- Players can click on grid cells to place their "X" or "O".
- Real-time win and tie detection.
- Scores are tracked for both players.
- Game restarts with a press of the spacebar.

## Installation

1. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
2. Clone this repository:
   ```sh
   git clone https://github.com/AlperErd0gan/XOX-Game.git
## Usage

1. When the game starts, press the spacebar to begin.
2. Click on the grid cells to place your symbol ("X" or "O").
3. The game will automatically detect wins or ties and display a message.
4. Press the spacebar to restart the game after a win or tie.

## Code Description

- **`screen`**: Sets up the Turtle graphics window.
- **`drawer`**: Responsible for drawing the game grid.
- **`player_turtle`**: Used to draw "X" and "O" on the grid.
- **`message_turtle`**: Displays messages on the screen.
- **`board`**: Keeps track of the current state of the grid.
- **`draw_grid()`**: Draws the 3x3 grid on the screen.
- **`draw_x(x, y)`**: Draws an "X" at the specified coordinates.
- **`draw_o(x, y)`**: Draws an "O" at the specified coordinates.
- **`check_win(player)`**: Checks if the current player has won.
- **`is_board_full()`**: Checks if the grid is full, indicating a tie.
- **`display_message_with_bg(message, bg_color)`**: Displays messages with background color.
- **`clear_message()`**: Clears any displayed message.
- **`click_handler(x, y)`**: Handles clicks on the grid and updates the game state.
- **`restart_game_from_space()`**: Resets the game when the spacebar is pressed.
- **`show_restart_screen()`**: Displays a message indicating the game is over and prompts for a restart.
- **`introduction()`**: Displays the introduction message and waits for the spacebar to start the game.
- **`start_game()`**: Initializes the game and sets up event listeners.

## Contributing

Feel free to submit issues or pull requests if you have any suggestions or improvements for the game.

