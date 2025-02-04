import pygame

"""
This script creates a simple game window using Pygame.

The script initializes Pygame, sets up a display window with a specified width and height,
and enters a main loop to keep the window open and listen for events. The window is filled
with a black background, and a red rectangle and a blue circle are drawn on it.

Modules:
    pygame: A set of Python modules designed for writing video games.

Functions:
    None

Variables:
    screen_width (int): The width of the game window.
    screen_height (int): The height of the game window.
    screen (pygame.Surface): The display surface for the game window.
    WHITE (tuple): RGB color value for white.
    BLACK (tuple): RGB color value for black.
    RED (tuple): RGB color value for red.
    GREEN (tuple): RGB color value for green.
    BLUE (tuple): RGB color value for blue.
    running (bool): A flag to control the main loop.
"""

pygame.init()  # Initialize all pygame modules

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Game Window")

# Color definitions
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

running = True

# Main loop to keep the window open and listen for events
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Drawing
    screen.fill(BLACK)

    # Draw a red rectangle
    pygame.draw.rect(screen, RED, (100, 100, 50, 50))

    # Draw a blue circle
    pygame.draw.circle(screen, BLUE, (300, 300), 50)

    pygame.display.flip()

pygame.quit()
