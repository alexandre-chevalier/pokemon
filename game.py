import pygame
from pokemon import POKEMONS

class Game:
    def __init__(self):
        """Initialisation de la fenêtre et des Pokémon"""
        pygame.init()
        self.width, self.height = 1200, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pokémon Battle")
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_started = False
        self.show_menu = False

        # 🔹 Chargement du fond
        self.background = pygame.image.load("images/background.jpg")
        self.background = pygame.transform.scale(self.background, (self.width, self.height))

        # 🔹 Chargement de la police
        self.font = pygame.font.Font("images/Audiowide-Regular.ttf", 40)
        self.small_font = pygame.font.Font("images/Audiowide-Regular.ttf", 20)

        # 🔹 Création des Pokémon
        self.pokemon1 = POKEMONS["Pikachu"](50, 50)
        self.pokemon2 = POKEMONS["Dracaufeu"](self.width - 100, self.height - 100)

        self.all_pokemons = [cls(0, 0) for cls in POKEMONS.values()]

        # 🔹 Variables pour gérer la navigation dans le menu
        self.menu_scroll = 0
        self.pokemon_per_row = 4
        self.pokemon_size = 80
        self.margin = 20

    def draw(self):
        """Affichage du fond, des Pokémon et du titre"""
        self.screen.blit(self.background, (0, 0))  # Affiche l’image de fond

        if self.show_menu:
            self.display_menu()
        elif self.game_started:
            # 🔹 Affichage des Pokémon uniquement si le jeu a démarré
            self.pokemon1.display(self.screen)
            self.pokemon2.display(self.screen)

        # 🔹 Affichage du titre
        title_text = self.font.render("Bienvenue dans Pokémon Battle", True, (0, 0, 0))
        self.screen.blit(title_text, (self.width // 2 - title_text.get_width() // 2, 50))

        pygame.display.flip()  # Met à jour l’écran

    def display_menu(self):
        """Affiche la liste des Pokémon avec images et noms"""
        menu_surface = pygame.Surface((self.width // 1.5, self.height // 1.5))
        menu_surface.fill((255, 255, 255))
        self.screen.blit(menu_surface, (self.width // 6, self.height // 6))

        title = self.font.render("Liste des Pokémon", True, (0, 0, 0))
        self.screen.blit(title, (self.width // 2 - title.get_width() // 2, self.height // 6 + 10))

        # 🔹 Affichage des Pokémon sous forme de grille
        x_offset = self.width // 6 + self.margin
        y_offset = self.height // 6 + 80
        col_count = 0

        for pokemon in self.all_pokemons[self.menu_scroll:]:
            # Affichage de l'image du Pokémon
            scaled_image = pygame.transform.scale(pokemon.image, (self.pokemon_size, self.pokemon_size))
            self.screen.blit(scaled_image, (x_offset, y_offset))

            # Affichage du nom du Pokémon
            text = self.small_font.render(pokemon.name, True, (0, 0, 0))
            self.screen.blit(text, (x_offset, y_offset + self.pokemon_size + 5))

            col_count += 1
            x_offset += self.pokemon_size + self.margin

            if col_count >= self.pokemon_per_row:
                col_count = 0
                x_offset = self.width // 6 + self.margin
                y_offset += self.pokemon_size + self.margin + 20

    def handle_events(self):
        """Gère les événements (fermeture du jeu, navigation dans le menu et touches spéciales)"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.show_menu = not self.show_menu
                elif event.key == pygame.K_j:
                    self.game_started = True
                    self.show_menu = False
                elif event.key == pygame.K_ESCAPE:
                    self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and self.show_menu:
                if event.button == 4:  # Molette haut
                    self.menu_scroll = max(0, self.menu_scroll - 1)
                elif event.button == 5:  # Molette bas
                    self.menu_scroll = min(len(self.all_pokemons) - self.pokemon_per_row, self.menu_scroll + 1)

    def run(self):
        """Boucle principale du jeu"""
        while self.running:
            self.handle_events()
            self.draw()
            self.clock.tick(60)
        pygame.quit()

# 📌 Lancer le jeu
if __name__ == "__main__":
    game = Game()
    game.run()
