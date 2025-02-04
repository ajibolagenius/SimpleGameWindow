import pygame

pygame.init()  # Initialize all pygame modules

# Set up the display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Game Window")

# Game Clock
clock = pygame.time.Clock()
FPS = 60

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
    pygame.draw.rect(
        screen, WHITE, (100, 100, 200, 200), 5
    )  # (surface, color, (x, y, width, height))

    # Draw a blue circle
    pygame.draw.circle(screen, BLUE, (300, 300), 50)  # (surface, color, center, radius)

    # Draw a green line
    pygame.draw.line(
        screen, GREEN, (50, 50), (750, 50), 5
    )  # (surface, color, start_pos, end_pos, width)

    # Draw a white ellipse
    pygame.draw.ellipse(
        screen, WHITE, (400, 400, 100, 200)
    )  # (surface, color, (x, y, width, height))

    # Draw a red polygon
    pygame.draw.polygon(
        screen, RED, [(500, 500), (600, 500), (550, 600)]
    )  # (surface, color, points)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
