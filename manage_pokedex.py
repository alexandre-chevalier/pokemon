import json
import pygame
import os
import random

# Pygame start
pygame.init()
pygame.font.init()
# Screen size
BASE_DIR = r"C:/Users/Windows/Desktop/projets/1a/pokemon"

# ways to files
IMAGE_DIR = os.path.join(BASE_DIR, "images")
SOUND_DIR = os.path.join(BASE_DIR, "sounds")



# Screen size
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

# background
background_image = pygame.image.load(os.path.join(IMAGE_DIR, 'tokyo.png')) 
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors used
BLACK = (0, 0, 0)
YELLOW = (255, 223, 0)
WHITE = (255, 255, 255)
DARK_BLUE = (0, 0, 128)
RED = (250, 0, 0)


font_path = os.path.join(BASE_DIR, "Audiowide-Regular.ttf")

class Pokedex:
    
    def __init__(self, name):
        
        self.name = name
        self.pokemon_list = []
        self.pokedex_list = []
        self.pokemon_met = [{'name': 'pikachu', 'lifePoint': 100, 'level': 1, 'experience': 0, 'giveXp': 10, 'limitXP': 20, 'attack': 10, 'defence': 8, 'type1': 'electric', 'type2': None, 'KO': False, 'link_image': 'images', 'statut': 'normal', 'next_evolution': {'name': 'raichu', 'lifePoint': 250, 'level': 1, 'experience': 0, 'giveXp': 100, 'limitXP': 120, 'attack': 30, 'defence': 25, 'type1': 'electric', 'type2': None, 'KO': False, 'link_image': 'images', 'statut': 'normal', 'next_evolution': None}}, 
                            
                            ]
        pygame.font.init()  # calls and manage fonts
        self.title_font = pygame.font.Font(font_path, 70)
        self.poke_font = pygame.font.Font(font_path, 36)
       
        # Calls screen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pokemon")
        
        self.back_button_rect = None  # Initialisation back button
# Display the score booard rectangle   
    def displayScore(self):
        
        
        scoreSurface = pygame.Surface((800,400),pygame.SRCALPHA)  
        scoreRect = scoreSurface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        pygame.draw.rect(scoreSurface, (0, 0,0, 128), (0, 0, 800, 400),border_radius=15)
        self.screen.blit(scoreSurface, scoreRect.topleft)
    
    def display_title(self):
        title_text = self.title_font.render("Pokedex", True, RED)
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
    
    def choose_pokemon_random(self):
        with open('pokemon.json', 'r') as file:#load all pokemons from pokemon.json
            self.pokemon_list = json.load(file)
       
        pokemon_sample = random.sample(self.pokemon_list, 4) # Randomly chooses 1 element from pokemon_list
        return pokemon_sample

# Build a deck randomly
    def deck_building(self):
        new_deck = self.choose_pokemon_random() # Calls the sample function
        return new_deck
    
     # Get pokedex from podex.json   
    def get_pokedex_list(self): # Get pokedex and create a pokedex if none
        try:
            with open('poke.json', 'r') as fichier:
                self.pokedex_list = json.load(fichier)
        except FileNotFoundError:
                self.pokedex_list = []
        return self.pokedex_list    
    

    
    def record_pokedex(self):
            self.get_pokedex_list()
            self.entry = {self.name : self.pokemon_met}
            self.pokedex_list.append(self.entry)
            with open('poke.json', 'w') as fichier:
                json.dump(self.pokedex_list, fichier,indent=4)
    
    def run(self):
            print("Méthode run() appelée")
            running = True
            
            self.back_button_rect = self.displayBlackButton()

            while running:

                self.screen.blit(background_image, (0, 0))  # Background
                
                # Display elements
                self.display_title()
                self.displayBlackButton()
                self.displayScore()
                
                pygame.display.flip()  # Update screen
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if self.back_button_rect.collidepoint(mouse_pos):# return to menu
                            from menu import Menu 
                            menu = Menu()
                            menu.run()  
                            running = False  # close window
                            
            pygame.quit()  

if __name__ == "__main__":

    player_name = input(" Joueur")
    pokedex= Pokedex(player_name)
    pokedex.record_pokedex()
    pokedex_list = pokedex.get_pokedex_list()
    print(pokedex_list)
        # pokedex.run() 


