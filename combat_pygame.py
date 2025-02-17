import pygame
import random
import json
import os
from pokémon import Pokemon

# Initialize Pygame
pygame.init()
pygame.font.init()

# Screen size
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 223, 0)


BASE_DIR = r"C:\Users\ndiay\Desktop\lptf\projets\pokemon\develop"
IMAGE_DIR = os.path.join(BASE_DIR, "images")
SOUND_DIR = os.path.join(BASE_DIR, "sounds")


font_path = os.path.join(BASE_DIR,"Audiowide-Regular.ttf")
font = pygame.font.Font(font_path, 36)


# List of possible opponent Pokémon
opponent_pokemon_list = [
    Pokemon("Salamèche", 100, 1, 0, 10, 20, 10, 8, "Feu", None, None),
    Pokemon("Carapuce", 100, 1, 0, 10, 20, 10, 8, "Eau", None, None),
    Pokemon("Bulbizarre", 100, 1, 0, 10, 20, 10, 8, "Plante", None, None),
    
]

class Combat:
    TYPE_EFFICACY = {
        ("Eau", "Feu"): 2, ("Feu", "Plante"): 2, ("Plante", "Eau"): 2,
        ("Feu", "Eau"): 0.5, ("Eau", "Plante"): 0.5, ("Plante", "Feu"): 0.5,
        ("Normal", "Normal"): 1, ("Eau", "Eau"): 1, ("Feu", "Feu"): 1,
    }

    def __init__(self, pokemon1):
        self.pokemon1 = pokemon1
        self.pokemon2 = random.choice(opponent_pokemon_list) 
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pokemon Battle")
        self.attack_button_rect = None

        # Load Pokémon images
        self.pokemon1_image = self.load_and_scale_image(self.pokemon1.name, (150, 150))
        self.pokemon2_image = self.load_and_scale_image(self.pokemon2.name, (150, 150))

    def load_and_scale_image(self, pokemon_name, size):
        try:
            image_path = os.path.join(IMAGE_DIR, f"{pokemon_name}.png")
            image = pygame.image.load(image_path)
            return pygame.transform.scale(image, size)
        except pygame.error as e:
            print(f"Error loading image: {e}")
            return None

    def display_characteristics(self):
        # Display Pokemon 1 characteristics
        pokemon1_info = font.render(
            f"{self.pokemon1.name} - HP: {self.pokemon1.lifePoint}, Attack: {self.pokemon1.attack}, Defense: {self.pokemon1.defence}, Type: {self.pokemon1.type1}",
            True, WHITE
        )
        self.screen.blit(pokemon1_info, (50, 50))

        # Display Pokemon 2 characteristics
        pokemon2_info = font.render(
            f"{self.pokemon2.name} - HP: {self.pokemon2.lifePoint}, Attack: {self.pokemon2.attack}, Defense: {self.pokemon2.defence}, Type: {self.pokemon2.type1}",
            True, WHITE
        )
        self.screen.blit(pokemon2_info, (50, 100))

        # Display Pokémon images
        if self.pokemon1_image:
            self.screen.blit(self.pokemon1_image, (50, 200))
        if self.pokemon2_image:
            self.screen.blit(self.pokemon2_image, (SCREEN_WIDTH - 200, 200))

    def calculate_multiplier(self, attacker, target):
        return self.TYPE_EFFICACY.get((attacker.type1, target.type1), 1)

    def attack(self, attacker, target):
        multiplier = self.calculate_multiplier(attacker, target)
        damage = max(0, (attacker.attack * multiplier) - target.defence)
        target.lifePoint -= damage
        print(f"{attacker.name} attacks {target.name} with a multiplier of {multiplier}. Damage dealt: {damage}")
        if target.lifePoint <= 0:
            target.KO = True
            print(f"{target.name} is K.O. !")

    def draw_attack_button(self):
        button_width = 200
        button_height = 50
        self.attack_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT - button_height - 20, button_width, button_height)
        pygame.draw.rect(self.screen, YELLOW, self.attack_button_rect, border_radius=10)

        # Button text
        attack_button_text = font.render("Attack", True, BLACK)
        attack_button_text_rect = attack_button_text.get_rect(center=self.attack_button_rect.center)
        self.screen.blit(attack_button_text, attack_button_text_rect)

    def display_turn(self, attacker_name):
        turn_info = font.render(f"{attacker_name}'s turn to attack!", True, WHITE)
        self.screen.blit(turn_info, (50, 150))

    def start_battle(self):
        running = True
        turn = 1  # 1 for Pokemon1's turn, 2 for Pokemon2's turn

        while running:
            self.screen.fill(BLACK)
            self.display_characteristics()
            self.draw_attack_button()

            # Display whose turn it is
            if turn == 1:
                self.display_turn(self.pokemon1.name)
            else:
                self.display_turn(self.pokemon2.name)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.attack_button_rect.collidepoint(event.pos):
                        if turn == 1:
                            self.attack(self.pokemon1, self.pokemon2)
                            turn = 2
                        else:
                            self.attack(self.pokemon2, self.pokemon1)
                            turn = 1

            if self.pokemon1.KO or self.pokemon2.KO:
                winner = self.pokemon1 if not self.pokemon1.KO else self.pokemon2
                print(f"The winner is {winner.name}!")
                running = False

            pygame.display.flip()

        pygame.quit()

# Example usage
pikachu = Pokemon("Pikachu", 100, 1, 0, 10, 20, 10, 8, "Eau", None, None)
combat = Combat(pikachu)
combat.start_battle()
