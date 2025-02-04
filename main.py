import pygame

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

    # Draw a green line
    pygame.draw.line(screen, GREEN, (50, 50), (750, 50), 5)

    # Draw a white ellipse
    pygame.draw.ellipse(screen, WHITE, (400, 400, 100, 200))

    # Draw a red polygon
    pygame.draw.polygon(screen, RED, [(500, 500), (600, 500), (550, 600)])

    pygame.display.flip()

pygame.quit()
