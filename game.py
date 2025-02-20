import pygame
import os
import sys
from player import Player

pygame.init()
pygame.font.init()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ways to files
IMAGE_DIR = os.path.join(BASE_DIR, "data/images")
SOUND_DIR = os.path.join(BASE_DIR, "data/sounds")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# Screen size
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

# Colors used
BLACK = (0, 0, 0)
YELLOW = (255, 223, 0)
WHITE = (255, 255, 255)
DARK_BLUE = (0, 0, 128)
RED = (250, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pokemon Game")

# Load background image
background_image = pygame.image.load(os.path.join(IMAGE_DIR, 'background2.jpg'))
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a player and choose a Pokémon
player = Player("Ash")
player.choose_pokemon("1")  # Assuming the player chooses the first Pokémon

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

    # Start a battle
    player.battle()
    running = False  # End the game loop after one battle for demonstration

# Quit pygame
pygame.quit()
sys.exit()