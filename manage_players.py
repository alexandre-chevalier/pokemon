import json
import pygame
import os
pygame.init()
pygame.font.init()

# Screen size
BASE_DIR = r"C:/Users/Windows/Desktop/projets/1a/pokemon"

# ways to files
IMAGE_DIR = os.path.join(BASE_DIR, "images")
SOUND_DIR = os.path.join(BASE_DIR, "sounds")

# Pygame start
pygame.init()
pygame.font.init()

# Screen size
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

# background
background_image = pygame.image.load(os.path.join(IMAGE_DIR, 'glory.png')) 
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors used
BLACK = (0, 0, 0)
YELLOW = (255, 223, 0)
WHITE = (255, 255, 255)
DARK_BLUE = (0, 0, 128)
RED = (250, 0, 0)

font_path = os.path.join(BASE_DIR, "Audiowide-Regular.ttf")

class History:
    def __init__(self, players_file):
        self.players_file = players_file

        pygame.font.init()  # S'assurer que le module de police est bien initialisé
        self.title_font = pygame.font.Font(font_path, 70)
        self.poke_font = pygame.font.Font(font_path, 36)

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pokemon")
        self.back_button_rect = None  # Initialisation de l'attribut du bouton

    def display_title(self):
        title_text = self.title_font.render("Scoreboard", True, RED)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 50))
        self.screen.blit(title_text, title_rect)

    # Create the "Back to Menu" button
    def displayBlackButton(self):   
        button_width = 220
        button_height = 40
        self.back_button_rect = pygame.Rect(10, self.screen.get_height() - button_height - 10, button_width, button_height)
        pygame.draw.rect(self.screen, YELLOW, self.back_button_rect, border_radius=15)

        # Button text
        back_button_text = self.poke_font.render("<<< Menu", True, DARK_BLUE)
        back_button_text_rect = back_button_text.get_rect(center=self.back_button_rect.center)
        self.screen.blit(back_button_text, back_button_text_rect)
        return self.back_button_rect
    
    def record_history(self, score, player_name):
        try:
            with open("players.json", "r") as f:
                players_container = json.load(f)
        except FileNotFoundError:
            players_container = []
        except json.JSONDecodeError:
            players_container = []
        
        player_found = False
        for player in players_container:
            if player["name"] == player_name:
                player["score"] += score
                player["pokedex"] = player_name
                player_found = True
                break
        
        if not player_found:
            players_container.append({"name": player_name, "score": score, "pokedex": player_name})
        
        players_container = sorted(players_container, key=lambda x: x["score"], reverse=True)
        
        with open("players.json", "w") as f:
            json.dump(players_container, f, indent=4)

    def get_player_history(self):
        with open("players.json", "r") as file:
            players_container = json.load(file)
        return players_container

    def run(self):
        print("Méthode run() appelée")
        running = True
        self.back_button_rect = self.displayBlackButton()
        mouse_pos = (0, 0)  # Ajout d'une valeur par défaut
        while running:
            self.screen.blit(background_image, (0, 0))  # Background
            # Display elements
            self.display_title()
            self.displayBlackButton()

            pygame.display.flip()  # Update screen
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.back_button_rect.collidepoint(mouse_pos):
                        from menu import Menu 
                        menu = Menu()
                        menu.run()  # Retour au menu
                        running = False  # Fermer la fenêtre actuelle
                        
        pygame.quit()  # Déplacer pygame.quit ici pour s'assurer qu'il est appelé lorsque la boucle est terminée


# Créer une instance de la classe History et lancer la méthode run
if __name__ == "__main__":
    history = History("players.json")
    history.run()
