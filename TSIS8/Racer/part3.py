import pygame

pygame.init()

# Setting up the screen
screen = pygame.display.set_mode((800, 600))

# Setting up the caption
pygame.display.set_caption("Pygame Tutorial Part 2")

# Setting up the clock
clock = pygame.time.Clock()

# Defining colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Setting up the game loop
running = True
while running:

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Filling the screen with color
    screen.fill(WHITE)

    # Drawing on the screen
    pygame.draw.rect(screen, RED, [400, 300, 50, 50])
    pygame.draw.line(screen, BLUE, [0, 0], [800, 600], 5)
    pygame.draw.ellipse(screen, GREEN, [200, 200, 250, 100])

    # Drawing text on the screen
    font = pygame.font.Font(None, 36)
    text = font.render("Hello World!", True, BLACK)
    screen.blit(text, [250, 250])

    # Updating the screen
    pygame.display.update()

    # Setting up the clock
    clock.tick(60)

# Quitting Pygame
pygame.quit()