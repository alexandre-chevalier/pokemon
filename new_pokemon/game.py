import pygame
import os
from battle_manager import BattleManager

# Initialize Pygame and the font module
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

BASE_DIR = r"C:\Users\ndiay\Desktop\new_pokemon"
IMAGE_DIR = os.path.join(BASE_DIR, "images")
SOUND_DIR = os.path.join(BASE_DIR, "sounds")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
background_image = pygame.image.load(os.path.join(IMAGE_DIR, 'arene_ring.png'))
font_path = os.path.join(ASSETS_DIR, 'Audiowide-Regular.ttf')
font = pygame.font.Font(font_path, 36)

class Game:
    def __init__(self, combat):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pokemon Battle")
        self.combat = combat
        self.attack_button_rect = None

    def draw_attack_button(self):
        button_width = 200
        button_height = 50
        self.attack_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT - button_height - 20, button_width, button_height)
        pygame.draw.rect(self.screen, YELLOW, self.attack_button_rect, border_radius=10)
        attack_button_text = font.render("Attack", True, BLACK)
        attack_button_text_rect = attack_button_text.get_rect(center=self.attack_button_rect.center)
        self.screen.blit(attack_button_text, attack_button_text_rect)

    def display_characteristics(self):
        pokemon1_info = font.render(
            f"{self.combat.pokemon1.name} - HP: {self.combat.pokemon1.lifePoint}, Attack: {self.combat.pokemon1.attack}, Defense: {self.combat.pokemon1.defence}, Type: {self.combat.pokemon1.type1}",
            True, WHITE
        )
        self.screen.blit(pokemon1_info, (50, 50))
        self.combat.display_status_effects(self.combat.pokemon1, 50, 80)
        pokemon2_info = font.render(
            f"{self.combat.pokemon2.name} - HP: {self.combat.pokemon2.lifePoint}, Attack: {self.combat.pokemon2.attack}, Defense: {self.combat.pokemon2.defence}, Type: {self.combat.pokemon2.type1}",
            True, WHITE
        )
        self.screen.blit(pokemon2_info, (50, 150))
        self.combat.display_status_effects(self.combat.pokemon2, 50, 180)
        if self.combat.pokemon1_image:
            self.screen.blit(self.combat.pokemon1_image, (100, 350))
        if self.combat.pokemon2_image:
            self.screen.blit(self.combat.pokemon2_image, (SCREEN_WIDTH - 300, 350))

    def run(self):
        running = True
        turn = 1
        while running:
            self.screen.blit(background_image, (0, 0))
            #self.display_characteristics()
            self.draw_attack_button()
            if turn == 1:
                self.combat.display_turn(self.combat.pokemon1.name)
                if self.combat.apply_status_effects(self.combat.pokemon1):
                    turn = 2
            else:
                self.combat.display_turn(self.combat.pokemon2.name)
                if self.combat.apply_status_effects(self.combat.pokemon2):
                    turn = 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.attack_button_rect.collidepoint(event.pos):
                        if turn == 1:
                            self.combat.attack(self.combat.pokemon1, self.combat.pokemon2)
                            turn = 2
                        else:
                            self.combat.attack(self.combat.pokemon2, self.combat.pokemon1)
                            turn = 1
            if self.combat.pokemon1.KO or self.combat.pokemon2.KO:
                winner = self.combat.pokemon1 if not self.combat.pokemon1.KO else self.combat.pokemon2
                looser = self.combat.pokemon1 if self.combat.pokemon1.KO else self.combat.pokemon2
                self.combat.display_winner(winner)
                self.combat.record_pokedex(self.combat.pokemon2)
                self.combat.display_end_message(winner, looser)
                print(f"The winner is {winner.name}!")
                
                if winner == self.combat.pokemon1:
                    BattleManager.record_winner(winner, looser)
                    
                else:
                    BattleManager.remove_loser_pokemon(looser)    
                    
                running = False
            pygame.display.flip()
        pygame.quit()
