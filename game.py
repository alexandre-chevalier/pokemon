import pygame
import json
from manage_pokemon_list import Pokemon_bank
from dresseur import Dresseur

class Game:
    def __init__(self):
        pygame.init()
        self.width, self.height = 1200, 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sélection des Pokémon")
        self.clock = pygame.time.Clock()
        self.running = True
        self.selected_pokemons = []

        # Charger les Pokémon depuis le fichier JSON
        self.pokemon_bank = Pokemon_bank("original_bank")
        self.pokemon_list = self.pokemon_bank.get_pokemon_list()

        # Charger les images des Pokémon
        self.load_pokemon_images()

        # Création du dresseur
        self.dresseur = Dresseur("Dresseur Joueur")

    def load_pokemon_images(self):
        """Charge les images des Pokémon en mémoire"""
        self.pokemon_images = []
        for pokemon in self.pokemon_list:
            try:
                image = pygame.image.load(pokemon["image_path"])
                image = pygame.transform.scale(image, (80, 80))  # Redimensionne l'image
                self.pokemon_images.append((pokemon, image))
            except pygame.error:
                print(f"Impossible de charger l'image pour {pokemon['name']}")

    def draw_pokemon_menu(self):
        """Affiche la liste des Pokémon sous forme de grille"""
        self.screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 30)
        x_offset, y_offset = 50, 50
        row_limit = 6  # Nombre de Pokémon par ligne
        col_count = 0

        for idx, (pokemon, image) in enumerate(self.pokemon_images):
            self.screen.blit(image, (x_offset, y_offset))
            text = font.render(pokemon["name"], True, (0, 0, 0))
            self.screen.blit(text, (x_offset, y_offset + 85))

            # Stocker la position pour la sélection
            pokemon["rect"] = pygame.Rect(x_offset, y_offset, 80, 80)

            x_offset += 120  # Espacement entre les images
            col_count += 1

            if col_count >= row_limit:
                col_count = 0
                x_offset = 50
                y_offset += 120  # Nouvelle ligne

    def handle_mouse_click(self, pos):
        """Gère la sélection des Pokémon lorsqu'on clique dessus"""
        for pokemon, _ in self.pokemon_images:
            if "rect" in pokemon and pokemon["rect"].collidepoint(pos):
                if len(self.selected_pokemons) < 6:
                    self.selected_pokemons.append(pokemon)
                    print(f"{pokemon['name']} ajouté à votre équipe!")
                else:
                    print("Vous avez déjà sélectionné 6 Pokémon.")

    def handle_events(self):
        """Gère les événements utilisateurs"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_click(event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and len(self.selected_pokemons) == 6:
                    self.assign_pokemon_to_dresseur()
                    self.running = False

    def assign_pokemon_to_dresseur(self):
        """Associe les Pokémon sélectionnés au dresseur"""
        for pokemon in self.selected_pokemons:
            self.dresseur.add_pokemon(pokemon)
        print(f"\nÉquipe du Dresseur {self.dresseur.player_name}:")
        self.dresseur.display_pokemonTeam()

    def run(self):
        """Boucle principale du jeu"""
        while self.running:
            self.handle_events()
            self.draw_pokemon_menu()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
