import pygame
import os
from manage_players import *

# Define BASE_DIR comme le dossier du fichier actuel
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ways to files
IMAGE_DIR = os.path.join(BASE_DIR, "images")
SOUND_DIR = os.path.join(BASE_DIR, "sounds")

# Pygame start
pygame.init()

# Screen size
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

# background
# Charger une image correctement avec BASE_DIR
background_image_path = os.path.join(IMAGE_DIR, "forest_ring.webp")
background_image = pygame.image.load(background_image_path)
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors used
BLACK = (0, 0, 0)
YELLOW = (255, 223, 0)
WHITE = (255, 255, 255)
DARK_BLUE = (0, 0, 128)
RED = (250, 0, 0)

class Menu:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pokemon")
        
        # Polices
        self.title_font = pygame.font.Font(os.path.join(ASSETS_DIR, "Audiowide-Regular.ttf"), 70)
        self.poke_font = pygame.font.Font(os.path.join(ASSETS_DIR, "Audiowide-Regular.ttf"), 36)
        
        # Options du menu
        self.menu_options = ["Play now", "History", "Scoreboard", "Exit"]
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        button_width = 400  
        button_height = 50  
        y_position = 250  # first button position
        
        for option in self.menu_options:
            text = self.poke_font.render(option, True, RED)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, y_position))
            button_rect = pygame.Rect(SCREEN_WIDTH // 2 - button_width // 2, text_rect.y - button_height // 2, button_width, button_height)
            
            # text on button position
            text_rect.center = button_rect.center
            
            self.buttons.append((option, button_rect, text, text_rect))
            y_position += 80  # space between ech button

    def draw_buttons(self):
        for _, button_rect, text, text_rect in self.buttons:
            # Button shape
            pygame.draw.rect(self.screen, YELLOW, button_rect, border_radius=15)  
            self.screen.blit(text, text_rect)

    def display_title(self):
        title_text = self.title_font.render("Pokemon", True, DARK_BLUE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 100))
        self.screen.blit(title_text, title_rect)

    def run(self):
        running = True
        while running:
            self.screen.blit(background_image, (0, 0))  # Background
            self.display_title()
            self.draw_buttons()
            pygame.display.flip()

            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for option, button_rect, _, _ in self.buttons:
                        if button_rect.collidepoint(mouse_pos):
                            if option == "Exit":
                                running = False
                            elif option == "Scoreboard":
                                history = History("players.json")
                                history.run()
                            else:
                                print(f"{option} sélectionné")
        
        pygame.quit()

# Lancer le menu
if __name__ == "__main__":
    menu = Menu()
    menu.run()
