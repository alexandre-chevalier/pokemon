import pygame

class Game:
    def __init__(self, width=1200, height=600, title="Pokémon Battle"):
        """Initialisation de la fenêtre de jeu"""
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)
        self.background = pygame.image.load("images/background.jpg")
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.font = pygame.font.Font("images/Audiowide-Regular.ttf", 40)  # Remplace par ta police
        self.clock = pygame.time.Clock()
        self.running = True

    def draw(self):
        """Affichage des éléments graphiques"""
        self.screen.blit(self.background, (0, 0))  # Afficher l’image de fond

        title_text = self.font.render("Bienvenue dans Pokémon Battle", True, (0, 0, 0))
        self.screen.blit(title_text, (self.width // 2 - title_text.get_width() // 2, 50))

        pygame.display.flip()  # Mettre à jour l'affichage

    def handle_events(self):
        """Gère les interactions clavier/souris"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False  # Quitter le jeu

    def run(self):
        """Boucle principale du jeu"""
        while self.running:
            self.handle_events()
            self.draw()
            self.clock.tick(60)  # 60 FPS

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
