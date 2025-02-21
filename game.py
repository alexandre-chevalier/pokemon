import os
import json
import pygame
import sys
import random
from player import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "data/images")
SOUND_DIR = os.path.join(BASE_DIR, "data/sounds")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
Pokemon_list = os.path.join(BASE_DIR, "data/pokemon.json")
player_list = os.path.join(BASE_DIR, "data/players.json")
poke_file = os.path.join(BASE_DIR, "data/poke.json")

# Initialiser le fichier poke.json avec un dictionnaire vide si nécessaire
if not os.path.exists(poke_file):
    with open(poke_file, 'w') as file:
        json.dump({}, file)
    print(f"Fichier {poke_file} initialisé avec succès.")
else:
    print(f"Fichier {poke_file} déjà existant.")

# Table des types (simplifiée pour l'exemple)
TYPE_MULTIPLIERS = {
    ("electric", "water"): 2.0,
    ("water", "fire"): 2.0,
    ("fire", "grass"): 2.0,
    ("grass", "water"): 2.0,
    ("fire", "water"): 0.5,
    ("water", "grass"): 0.5,
    ("grass", "fire"): 0.5
}

class Game:
    def __init__(self, width, height, background_image_path, player):
        pygame.init()
        pygame.mixer.init()
        background_music_path = os.path.join(SOUND_DIR, "SuicuneBattle.wav")  # Remplace avec le bon fichier
        if os.path.exists(background_music_path):
            pygame.mixer.music.load(background_music_path)
            pygame.mixer.music.set_volume(0.5)  # Volume entre 0.0 et 1.0
            pygame.mixer.music.play(-1)  # -1 signifie que la musique tourne en boucle
        else:
            print("Fichier audio introuvable ! Vérifiez le chemin.")

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pokemon Game")

        self.background = pygame.image.load(background_image_path)
        self.background = pygame.transform.scale(self.background, (self.width, self.height))

        self.player = player
        self.font = pygame.font.Font(None, 36)
        self.running = True

        self.opponent_pokemon = self.choose_random_pokemon()

        self.attack_button = pygame.Rect(self.width // 2 - 50, self.height - 100, 100, 50)
        self.attacking = False
        self.attack_frame = 0

        self.player_pokemon = self.player.pokemon
        self.player_pokemon["current_hp"] = self.player_pokemon["lifePoint"]
        self.opponent_pokemon["current_hp"] = self.opponent_pokemon["lifePoint"]

        self.load_pokemon_images()

    def choose_random_pokemon(self):
        try:
            with open(Pokemon_list, 'r') as file:
                pokemon_list = json.load(file)
                return random.choice(pokemon_list)
        except FileNotFoundError:
            print("Le fichier des Pokémon n'a pas été trouvé.")
            return None

    def load_pokemon_images(self):
        player_image_path = os.path.join(IMAGE_DIR, f"{self.player_pokemon['name'].lower()}.png")
        opponent_image_path = os.path.join(IMAGE_DIR, f"{self.opponent_pokemon['name'].lower()}.png")

        if os.path.exists(player_image_path):
            self.player_pokemon_image = pygame.image.load(player_image_path)
            self.player_pokemon_image = pygame.transform.scale(self.player_pokemon_image, (150, 150))
        else:
            self.player_pokemon_image = None

        if os.path.exists(opponent_image_path):
            self.opponent_pokemon_image = pygame.image.load(opponent_image_path)
            self.opponent_pokemon_image = pygame.transform.scale(self.opponent_pokemon_image, (150, 150))
        else:
            self.opponent_pokemon_image = None

    def calculate_damage(self, attacker, defender):
        base_damage = max(attacker["attack"] - defender["defence"], 1)
        multiplier = TYPE_MULTIPLIERS.get((attacker["type1"], defender["type1"]), 1.0)
        return int(base_damage * multiplier)

    def attack(self):
        damage = self.calculate_damage(self.player_pokemon, self.opponent_pokemon)
        self.opponent_pokemon["current_hp"] -= damage
        if self.opponent_pokemon["current_hp"] <= 0:
            self.opponent_pokemon["KO"] = True

        opponent_damage = self.calculate_damage(self.opponent_pokemon, self.player_pokemon)
        self.player_pokemon["current_hp"] -= opponent_damage
        if self.player_pokemon["current_hp"] <= 0:
            self.player_pokemon["KO"] = True

    def draw_attack_button(self):
        pygame.draw.rect(self.screen, (255, 0, 0), self.attack_button)
        text_surface = self.font.render("Attaque", True, pygame.Color('white'))
        self.screen.blit(text_surface, (self.attack_button.x + 10, self.attack_button.y + 10))

    def draw_health_bars(self):
        player_hp_text = self.font.render(f"PV: {self.player_pokemon['current_hp']}", True, pygame.Color('white'))
        opponent_hp_text = self.font.render(f"PV: {self.opponent_pokemon['current_hp']}", True, pygame.Color('white'))

        self.screen.blit(player_hp_text, (50, self.height - 220))
        self.screen.blit(opponent_hp_text, (self.width - 200, 30))

    def capture_pokemon(self):
        print(f"Vous avez capturé {self.opponent_pokemon['name']} !")

        # Ajouter le Pokémon capturé à la liste du joueur
        if "captured_pokemon" not in self.player.__dict__:
            self.player.captured_pokemon = []

        self.player.captured_pokemon.append(self.opponent_pokemon)

        # Sauvegarde les données du joueur
        self.player.save_to_file()

        # Sauvegarde les Pokémon rencontrés
        self.save_encountered_pokemon()

    def save_encountered_pokemon(self):
        try:
            if os.path.exists(poke_file):
                with open(poke_file, 'r') as file:
                    encountered_pokemon = json.load(file)
            else:
                encountered_pokemon = {}

            if self.player.name not in encountered_pokemon:
                encountered_pokemon[self.player.name] = []

            encountered_pokemon[self.player.name].append(self.opponent_pokemon)

            with open(poke_file, 'w') as file:
                json.dump(encountered_pokemon, file, indent=4)

            print(f"Pokémon rencontré enregistré avec succès dans {poke_file}.")

        except Exception as e:
            print(f"Erreur lors de la sauvegarde des Pokémon rencontrés : {e}")

    def check_game_over(self):
        if self.player_pokemon["KO"]:
            self.display_end_screen("GAME OVER", (255, 0, 0))  # Rouge si on perd
        elif self.opponent_pokemon["KO"]:
            self.capture_pokemon()  # Capture du Pokémon si on gagne
            self.display_end_screen("VICTOIRE !", (0, 255, 0))  # Vert si on gagne

    def display_end_screen(self, message, color):
        self.screen.fill((0, 0, 0))  # Fond noir
        text_surface = self.font.render(message, True, color)
        self.screen.blit(text_surface, (self.width // 2 - 100, self.height // 2))
        pygame.display.flip()
        pygame.time.delay(3000)  # Pause de 3 secondes avant de quitter
        self.running = False

    def draw_pokemon(self):
        if self.player_pokemon_image:
            self.screen.blit(self.player_pokemon_image, (50, self.height - 200))
        if self.opponent_pokemon_image:
            self.screen.blit(self.opponent_pokemon_image, (self.width - 200, 50))

    def return_to_menu(self):
        self.running = False

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.attack_button.collidepoint(event.pos) and not self.opponent_pokemon["KO"]:
                        self.attack()

            self.screen.blit(self.background, (0, 0))
            self.draw_pokemon()
            self.draw_attack_button()
            self.check_game_over()
            self.draw_health_bars()
            pygame.display.flip()

        pygame.mixer.music.stop()
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
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
            print("Aucun Pokémon n'a pas été choisi.")
            sys.exit()

    game = Game(1200, 600, os.path.join(IMAGE_DIR, 'background1.jpg'), player)
    game.run()
