import pygame
import os
import sys
from player import Player

# Initialisation de pygame
pygame.init()
pygame.mixer.init()  # Initialisation du module audio

# Définition des constantes
WIDTH, HEIGHT = 1200, 600
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "data/images")
SOUND_DIR = os.path.join(BASE_DIR, "data/sounds")
MENU_BACKGROUND_IMAGE = os.path.join(IMAGE_DIR, "imput_name.jpg")
MENU_MUSIC = os.path.join(SOUND_DIR, "LugiaSong.wav")  # Ajout du chemin de la musique

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokemon Game Menu")

# Chargement de la musique du menu
if os.path.exists(MENU_MUSIC):
    pygame.mixer.music.load(MENU_MUSIC)
    pygame.mixer.music.set_volume(0.9)
    pygame.mixer.music.play(-1)  # Lecture en boucle
else:
    print("Fichier audio du menu introuvable !")

# Chargement de l'image de fond du menu
if os.path.exists(MENU_BACKGROUND_IMAGE):
    background = pygame.image.load(MENU_BACKGROUND_IMAGE)
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
else:
    print("Image d'arrière-plan du menu introuvable !")
    background = None

# Police
font = pygame.font.Font(None, 72)
button_font = pygame.font.Font(None, 50)

def draw_button(text, x, y, color):
    button_rect = pygame.Rect(x, y, 250, 60)
    pygame.draw.rect(screen, color, button_rect)
    text_surface = button_font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)
    return button_rect

def menu():
    running = True
    while running:
        screen.fill(BLACK)
        if background:
            screen.blit(background, (0, 0))
        
        # Titre du jeu
        title_text = font.render("Pokemon Game", True, WHITE)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))
        
        # Boutons
        start_button = draw_button("Jouer", WIDTH // 2 - 125, 300, GREEN)
        quit_button = draw_button("Quitter", WIDTH // 2 - 125, 400, RED)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    print("Lancement du jeu...")
                    from game import Game  # Import ici pour éviter les boucles
                    player_name = Player.ask_for_name()
                    player = Player(player_name)
                    if player.player_exists():
                        print(f"Le joueur {player_name} existe déjà avec le Pokémon {player.pokemon['name']}.")
                    else:
                        chosen_pokemon = player.display_pokemon_list()
                        if chosen_pokemon:
                            player.set_pokemon(chosen_pokemon)
                            player.save_to_file()
                            print(f"Le joueur {player_name} a choisi {chosen_pokemon['name']} et a été enregistré.")
                        else:
                            print("Aucun Pokémon choisi.")
                            sys.exit()
                    pygame.mixer.music.stop()  # Arrêt de la musique du menu avant de lancer le jeu
                    game = Game(WIDTH, HEIGHT, os.path.join(IMAGE_DIR, "background1.jpg"), player)
                    game.run()
                    running = False
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
        
        pygame.display.flip()

menu()
pygame.quit()