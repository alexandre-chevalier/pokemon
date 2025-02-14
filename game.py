import pygame
import sys
from player import Player
from pokemon import Pokemon
from menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 600))
        pygame.display.set_caption("Pokemon Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = "menu"
        self.player = Player("Ash")
        self.menu = Menu(self.player, self.screen)

    def main_menu(self):
        while self.state == "menu":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.state = "quit"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.state = "choose_pokemon"

            self.screen.fill((0, 0, 0))
            self.display_text("Main Menu - Press Enter to Choose Pokémon", 40, (255, 255, 255), 600, 300)
            pygame.display.flip()
            self.clock.tick(60)

    def choose_pokemon(self):
        self.menu.display_menu()
        self.state = "battle"

    def battle_mode(self):
        while self.state == "battle":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.state = "quit"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.state = "menu"

            self.screen.fill((0, 0, 0))
            self.display_text("Battle Mode - Press Esc to Return to Menu", 40, (255, 255, 255), 600, 300)
            pygame.display.flip()
            self.clock.tick(60)

    def display_text(self, text, size, color, x, y):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)

    def run(self):
        while self.running:
            if self.state == "menu":
                self.main_menu()
            elif self.state == "choose_pokemon":
                self.choose_pokemon()
            elif self.state == "battle":
                self.battle_mode()
            elif self.state == "quit":
                self.running = False

        pygame.quit()
        sys.exit()

# Example usage
if __name__ == "__main__":
    game = Game()
    game.run()