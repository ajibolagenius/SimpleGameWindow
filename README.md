# Pygame Simple Game Window Script

This script creates a simple game window using Pygame.

The script initializes Pygame, sets up a display window with a specified width and height, and enters a main loop to keep the window open and listen for events. The window is filled with a black background, and various shapes (rectangle, circle, line, ellipse, and polygon) are drawn on it.

## Modules

- `pygame`: A set of Python modules designed for writing video games.

## Functions

- None

## Variables

- `SCREEN_WIDTH` (int): The width of the game window.
- `SCREEN_HEIGHT` (int): The height of the game window.
- `screen` (pygame.Surface): The display surface for the game window.
- `WHITE` (tuple): RGB color value for white.
- `BLACK` (tuple): RGB color value for black.
- `RED` (tuple): RGB color value for red.
- `GREEN` (tuple): RGB color value for green.
- `BLUE` (tuple): RGB color value for blue.
- `FPS` (int): Frames per second for the game loop.
- `clock` (pygame.time.Clock): Clock object to control the frame rate.
- `running` (bool): A flag to control the main loop.

## Environment Setup

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. Install Pygame using pip:
    ```sh
    pip install pygame
    ```

## How to Run the Application

1. Navigate to the directory containing the [main.py](main.py) file.
2. Run the script using Python:
    ```sh
    python main.py
    ```
