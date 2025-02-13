import pygame
import os


BASE_DIR = r"C:/Users/Windows/Desktop/projets/1a/pokemon"

# Chemins vers les fichiers spécifiques
IMAGE_DIR = os.path.join(BASE_DIR, "images")
SOUND_DIR = os.path.join(BASE_DIR, "sounds")

# IPygame start
pygame.init()

# Sreen size
screen_resolution = (1200, 600)

class Menu:
    def __init__(self):
        self.screen = pygame.display.set_mode(screen_resolution)
        pygame.display.set_caption("Pokemon")
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.gray = (100, 100, 100)
        self.title_font = pygame.font.Font(os.path.join(BASE_DIR, "Audiowide-Regular.ttf"), 55)
        self.poke_font = pygame.font.Font(os.path.join(BASE_DIR, "Audiowide-Regular.ttf"), 36)
        self.menu_options = ["Play now", "History", "Scoreboard", "Exit"]
        self.selected_index = 0
        
    def display_title(self):
        title_text = self.title_font.render("Pokemon", True, self.black)
        title_rect = title_text.get_rect(center=(screen_resolution[0] // 2, 100))
        self.screen.blit(title_text, title_rect)

    def run(self):
        running = True
        while running:
            self.screen.fill(self.white)
            self.display_title()

            # Affichage des options du menu
            for i, option in enumerate(self.menu_options):
                color = self.black if i == self.selected_index else self.gray
                text = self.poke_font.render(option, True, color)
                text_rect = text.get_rect(center=(screen_resolution[0] // 2, 200 + 60 * i))
                self.screen.blit(text, text_rect)

            pygame.display.flip()

            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_index = (self.selected_index - 1) % len(self.menu_options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_index = (self.selected_index + 1) % len(self.menu_options)
                    elif event.key == pygame.K_RETURN:
                        if self.menu_options[self.selected_index] == "Exit":
                            running = False
        
        pygame.quit()

# Lancer le menu
if __name__ == "__main__":
    menu = Menu()
    menu.run()

