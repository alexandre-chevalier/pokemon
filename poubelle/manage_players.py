import json
import pygame
import os
from menu import *


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

   # def scores_history(BASE_DIR):
    #    score_hist= []
     #   with open (os.path.join(BASE_DIR,"score.json"), "r") as f:
      #          player_list= json.load(f)      
      #  for i, player in enumerate(player_list):
       # score_hist.append(f'{i+1}. {player["name"]} => {player["score"]}')
        #return score_hist   

    def display_title(self):
        title_text = self.title_font.render("Scoreboard", True, RED)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 50))
        self.screen.blit(title_text, title_rect)

    
    # Create the "Back to Menu" button
    def displayBlackButton(self):   
        
        button_width = 220
        button_height = 40
        back_button_rect = pygame.Rect(10, self.screen.get_height() - button_height - 10, button_width, button_height)
        pygame.draw.rect(self.screen, YELLOW, back_button_rect, border_radius=15)
        
        # Button text
        back_button_text  = self.poke_font.render("<<< Menu", True, DARK_BLUE)
        back_button_text_rect = back_button_text.get_rect(center=back_button_rect.center)
        self.screen.blit(back_button_text, back_button_text_rect)
        return back_button_rect

    
    def record_history(score, player_name):
            
            try:
                with open("players.json", "r") as f:
                    players_container = json.load(f)
            except FileNotFoundError:
                # if the file doesn't exist=> a new list
                players_container = []
            except json.JSONDecodeError:
                # if the file is not good => a new list
                players_container = []
            
            # update player or add a new player
            player_found = False
            for player in players_container:
                if player["name"] == player_name:
                    player["score"] += score
                    player["pokedex"] = player_name
                    player_found = True
                    break
            
            if not player_found:
                players_container.append({"name": player_name, "score": score, "pokedex" : player_name})
            
            # Trier les scores par ordre décroissant
            players_container = sorted(players_container, key=lambda x: x["score"], reverse=True)
            
            # Enregistrer les scores dans le fichier
            with open("players.json", "w") as f:
                json.dump(players_container, f, indent=4)  # indent=4 pour un formatage lisible

    def get_player_history():
        with open ("players.json", "r") as file:
            players_container = json.load(file)      
    
    def run(self):
        running = True
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
                    for option, button_rect, _, _ in self.buttons:
                        if button_rect.collidepoint(mouse_pos):
          
                                print(f"{option} sélectionné")
  
            
    pygame.quit()

# Créer une instance de la classe History et lancer la méthode run
history = History("players.json")
history.run()