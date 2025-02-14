import pygame
from player import Player
from pokemon import Pokemon

class Menu:
    def __init__(self, player, screen):
        self.player = player
        self.screen = screen
        self.font = pygame.font.Font(None, 36)

    def display_menu(self):
        menu_running = True
        while menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.display_team()
                    elif event.key == pygame.K_2:
                        self.choose_pokemon()
                    elif event.key == pygame.K_3:
                        menu_running = False

            self.screen.fill((0, 0, 0))
            self.display_text("Main Menu", 40, (255, 255, 255), 600, 100)
            self.display_text("1. Display Pokémon Team", 30, (255, 255, 255), 600, 200)
            self.display_text("2. Choose Pokémon for Battle", 30, (255, 255, 255), 600, 250)
            self.display_text("3. Exit", 30, (255, 255, 255), 600, 300)
            pygame.display.flip()

    def display_team(self):
        self.screen.fill((0, 0, 0))
        self.display_text(f"{self.player.name}'s Pokémon Team:", 40, (255, 255, 255), 600, 50)
        y_offset = 100
        for pokemon in self.player.pokemons:
            self.display_text(str(pokemon), 30, (255, 255, 255), 600, y_offset)
            y_offset += 50
        pygame.display.flip()
        pygame.time.wait(3000)

    def choose_pokemon(self):
        choosing = True
        while choosing:
            self.screen.fill((0, 0, 0))
            self.display_text("Choose a Pokémon for Battle:", 40, (255, 255, 255), 600, 50)
            y_offset = 100
            pokemon_rects = []
            for pokemon in self.player.pokemons:
                image = pygame.image.load(pokemon.link_image)
                image = pygame.transform.scale(image, (100, 100))
                image_rect = image.get_rect(center=(600, y_offset + 50))
                self.screen.blit(image, image_rect)
                text_surface, text_rect = self.display_text(pokemon.name, 30, (255, 255, 255), 600, y_offset)
                pokemon_rects.append((pokemon, image_rect))
                y_offset += 150
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    choosing = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for pokemon, rect in pokemon_rects:
                        if rect.collidepoint(mouse_pos):
                            self.screen.fill((0, 0, 0))
                            self.display_text(f"Chosen Pokémon: {pokemon.name}", 30, (255, 255, 255), 600, 400)
                            pygame.display.flip()
                            pygame.time.wait(3000)
                            choosing = False
                            break

    def display_text(self, text, size, color, x, y):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)
        return text_surface, text_rect

# Example usage
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("Pokemon Menu")

    player = Player("Ash")
    pikachu = Pokemon("Pikachu", 100, 1, 0, 10, 20, 10, 8, "electric", None, None)
    charmander = Pokemon("Charmander", 100, 1, 0, 10, 20, 10, 8, "fire", None, None)

    player.add_pokemon(pikachu)
    player.add_pokemon(charmander)

    menu = Menu(player, screen)
    menu.display_menu()

    pygame.quit()