import pygame

class Dresseur:
    def __init__(self, player_name, pokemonTeam=None):
        """Initialise un dresseur avec un nom et une équipe de Pokémon."""
        self.player_name = player_name
        self.pokemonTeam = pokemonTeam if pokemonTeam is not None else []

    def add_pokemon(self, pokemon):
        """Ajoute un Pokémon à l'équipe du dresseur (max 6)."""
        if len(self.pokemonTeam) < 6:
            self.pokemonTeam.append(pokemon)
            print(f"{pokemon.nom} a été ajouté à l'équipe de {self.player_name}!")
        else:
            print(f"{self.player_name} ne peut pas avoir plus de 6 Pokémon dans son équipe!")

    def display_pokemonTeam(self):
        """Affiche les Pokémon de l'équipe du dresseur."""
        print(f"The team of {self.player_name} is:")
        if not self.pokemonTeam:
            print("Aucun Pokémon dans l'équipe.")
        for index, pokemon in enumerate(self.pokemonTeam):
            print(f"{index + 1}. {pokemon.nom} (PV: {pokemon.pv}/{pokemon.pv_max})")

    def display_pokemonTeam_pygame(self, screen, font):
        """Affiche l'équipe du dresseur dans la fenêtre Pygame."""
        y_offset = 50
        for pokemon in self.pokemonTeam:
            texte = font.render(f"{pokemon.nom} - PV: {pokemon.pv}/{pokemon.pv_max}", True, (255, 255, 255))
            screen.blit(texte, (50, y_offset))
            y_offset += 30

class Game:
    def __init__(self, width = 800, height = 600):
        """Initialise la fenêtre Pygame."""
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height)) # Crée la fenêtre
        pygame.display.set_caption("Pokémon") # Définit le titre de la fenêtre
        self.clock = pygame.time.Clock()
        self.running = True
        self.state= "menu"
        self.font = pygame.font.Font(None, 40)

    def run(self):
        """Boucle principale du jeu."""
        while self.running:
            self.clock.tick(60) # Limite le jeu à 60 images par secondes

Game().run() # Crée une instance de la classe Game et lance la boucle principale du jeu                       