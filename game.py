# game.py
import pygame
from manage_pokemon_list import Pokemon_bank
from dresseur import Dresseur

class Game:
    def __init__(self):
        pygame.init()
        self.width, self.height = 1200, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pokémon Battle")
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_started = False
        self.show_menu = False

        # Chargement des Pokémon depuis Pokemon_bank
        self.pokemon_bank = Pokemon_bank("original_bank")
        self.pokemon_list = self.pokemon_bank.get_pokemon_list()

        # Création d'un dresseur
        self.dresseur = Dresseur("Nom du Dresseur")

    def run(self):
        """Boucle principale du jeu"""
        self.dresseur.choose_pokemons(self.pokemon_list)  # Permet au joueur de choisir ses Pokémon

        # Affichage de l'équipe du dresseur
        self.dresseur.display_pokemonTeam()

        while self.running:
            self.handle_events()
            self.screen.fill((255, 255, 255))
            self.display_menu()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

    def handle_events(self):
        """Gère les événements de sélection de Pokémon et autres interactions"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def display_menu(self):
        """Affiche le menu"""
        pass

if __name__ == "__main__":
    game = Game()
    game.run()
