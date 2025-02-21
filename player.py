import os
import json
import pygame

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "data/images")
SOUND_DIR = os.path.join(BASE_DIR, "data/sounds")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
Pokemon_list = os.path.join(BASE_DIR, "data/pokemon.json")
player_list = os.path.join(BASE_DIR, "data/players.json")

class Player:
    def __init__(self, name):
        self.name = name
        self.pokemon_file = Pokemon_list
        self.player_file = player_list
        self.pokemon = None
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 600))
        pygame.display.set_caption("Pokemon Game")
        self.font = pygame.font.Font(None, 36)
        self.background_image = None

    def player_exists(self):
        if os.path.exists(self.player_file):
            try:
                with open(self.player_file, 'r') as file:
                    players = json.load(file)
                    for player in players:
                        if player['name'] == self.name:
                            self.pokemon = player['pokemon']
                            return True
            except json.JSONDecodeError:
                return False
        return False

    def choose_pokemon(self, choice):
        try:
            with open(self.pokemon_file, 'r') as file:
                pokemon_list = json.load(file)
        except FileNotFoundError:
            print("Le fichier des Pokémon n'a pas été trouvé.")
            return None

        if choice.isdigit() and 1 <= int(choice) <= len(pokemon_list):
            chosen_pokemon = pokemon_list[int(choice) - 1]
            self.pokemon = chosen_pokemon
            return chosen_pokemon
        else:
            print("Entrée invalide. Veuillez entrer un numéro valide.")
            return None
        
    def get_captured_pokemon(self):
    
        try:
            with open(self.player_file, 'r') as file:
                players = json.load(file)
                for player in players:
                    if player['name'] == self.name:
                        return player.get('captured_pokemon', [])
        except (FileNotFoundError, json.JSONDecodeError):
                return []
        return []


    def save_to_file(self):
        player_data = {
            "name": self.name,
            "pokemon": self.pokemon,
            "score": 0,
            "captured_pokemon": getattr(self, "captured_pokemon", [])  # Vérifie si l'attribut existe
            }

        try:
            with open(player_list, 'r') as file:
                data = json.load(file)
                if not isinstance(data, list):  # Vérifie que data est bien une liste
                    data = []
        except (FileNotFoundError, json.JSONDecodeError):  # Si le fichier est vide ou invalide
            data = []

        for player in data:
            if player["name"] == self.name:
                player.update(player_data)
                break
        else:
            data.append(player_data)

        with open(player_list, 'w') as file:
            json.dump(data, file, indent=4)

        print(f"Les données de {self.name} ont été sauvegardées avec succès.")


    def set_pokemon(self, pokemon):
        self.pokemon = pokemon
        if not hasattr(self, "captured_pokemon"):
            self.captured_pokemon = []
        if pokemon not in self.captured_pokemon:
            self.captured_pokemon.append(pokemon)

        self.save_to_file()


    def change_background(self, image_path):
        self.background_image = pygame.image.load(image_path)
        self.background_image = pygame.transform.scale(self.background_image, (1200, 600))
        self.screen.blit(self.background_image, (0, 0))
        pygame.display.flip()

    @staticmethod
    def ask_for_name():
        pygame.init()
        screen = pygame.display.set_mode((1200, 600))
        pygame.display.set_caption("Entrez votre nom")
        font = pygame.font.Font(None, 100)
        title_surface = font.render("Entrez votre nom", True, pygame.Color('white'))
        title_width = title_surface.get_width()
        input_box = pygame.Rect((1200 - title_width) // 2 + 50, 300, title_width + 100, 60)  # Centered rectangle, moved right by 50 pixels
        color_inactive = pygame.Color('yellow')
        color_active = pygame.Color('yellow')
        color = color_inactive
        active = False
        text = ''
        done = False

        # Load background image
        background_image = pygame.image.load(os.path.join(IMAGE_DIR, 'imput_name.jpg'))
        background_image = pygame.transform.scale(background_image, (1200, 600))

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive
                elif event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            done = True
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            screen.blit(background_image, (0, 0))  # Draw background image
            # Render the text "Entrez votre nom"
            screen.blit(title_surface, ((1200 - title_width) // 2, 200))  # Position above the input box
            # Render the input text
            txt_surface = font.render(text, True, pygame.Color('white'))
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            pygame.draw.rect(screen, color, input_box, 2)

            pygame.display.flip()

        pygame.quit()
        return text

    def display_pokemon_list(self):
        try:
            with open(self.pokemon_file, 'r') as file:
                pokemon_list = json.load(file)
        except FileNotFoundError:
            print("Le fichier des Pokémon n'a pas été trouvé.")
            return None

        self.change_background(os.path.join(IMAGE_DIR, 'glory.png'))

        done = False
        chosen_pokemon = None
        pokemon_rects = []

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        done = True
                    elif event.key == pygame.K_ESCAPE:
                        done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for index, rect in enumerate(pokemon_rects):
                        if rect.collidepoint(mouse_pos):
                            chosen_pokemon = pokemon_list[index]
                            done = True
                            break

            self.screen.blit(self.background_image, (0, 0))  # Draw background image

            # Display Pokémon in a grid format
            pokemon_rects = []
            for index, pokemon in enumerate(pokemon_list):
                row = index // 5
                col = index % 5
                x = 50 + col * 220
                y = 50 + row * 120

                # Load Pokémon image
                pokemon_image_path = os.path.join(IMAGE_DIR, f"{pokemon['name'].lower()}.png")
                if os.path.exists(pokemon_image_path):
                    pokemon_image = pygame.image.load(pokemon_image_path)
                    pokemon_image = pygame.transform.scale(pokemon_image, (100, 100))
                    self.screen.blit(pokemon_image, (x, y))
                    pokemon_rects.append(pokemon_image.get_rect(topleft=(x, y)))
                else:
                    print(f"Image not found for {pokemon['name']} at {pokemon_image_path}")

                # Display Pokémon name
                pokemon_text = f"{index + 1}. {pokemon['name']}"
                text_surface = self.font.render(pokemon_text, True, pygame.Color('white'))
                self.screen.blit(text_surface, (x, y + 100))

            pygame.display.flip()

        return chosen_pokemon

    def update(self):
        # Update player state
        pass

    def draw(self, screen):
        # Draw player on the screen
        pass

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
            print("Aucun Pokémon n'a été choisi.")
            sys.exit()