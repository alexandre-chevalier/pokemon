import pygame, os, sys


pygame.init()

# Set up the display
screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pokemon Game")

# Load background image
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "data\images")
background_image = pygame.image.load(os.path.join(IMAGE_DIR, 'background2.png'))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background
    screen.blit(background_image, (0, 0))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()