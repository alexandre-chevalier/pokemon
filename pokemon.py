import pygame
import json
import os
from input_add_pokemon import InputBox

# Initialisation de Pygame
pygame.init()

# Dimensions de l'écran
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 223, 0)

# Chemins des fichiers
BASE_DIR = r"C:/Users/Windows/Desktop/projets/1a/pokemon"
IMAGE_DIR = os.path.join(BASE_DIR, "images")
SOUND_DIR = os.path.join(BASE_DIR, "sounds")
font_path = os.path.join(BASE_DIR, "Audiowide-Regular.ttf")
font = pygame.font.Font(font_path, 36)

# Création de la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ajouter un Pokémon")

class Pokemon:
    def __init__(self, name, lifePoint, level, XP, giveXP, limitXP, attack, defence, type1, type2, next_evolution):
        self.name = name
        self.lifePoint = lifePoint
        self.level = level
        self.experience = XP
        self.giveXp = giveXP
        self.limitXP = limitXP
        self.attack = attack
        self.defence = defence
        self.type1 = type1
        self.type2 = type2
        self.KO = False
        self.link_image = "images"
        self.statut = "normal"
        self.next_evolution = next_evolution
        self.pokemon_list = self.get_pokemon_list()
        self.status_effects = {}

    def add_status_effect(self, effect, duration):
        self.status_effects[effect] = duration

    def decrement_status_effects(self):
        effects_to_remove = []
        for effect, duration in self.status_effects.items():
            if duration > 1:
                self.status_effects[effect] = duration - 1
            else:
                effects_to_remove.append(effect)
        for effect in effects_to_remove:
            del self.status_effects[effect]

    def evolve(self, pokemon):
        if pokemon:
            self.name = pokemon.name
            self.lifePoint = pokemon.lifePoint
            self.level = pokemon.level
            self.experience = pokemon.experience
            self.giveXp = pokemon.giveXp
            self.limitXP = pokemon.limitXP
            self.attack = pokemon.attack
            self.defence = pokemon.defence
            self.type1 = pokemon.type1
            self.type2 = pokemon.type2
            self.next_evolution = pokemon.next_evolution

    def attacks(self):
        return (self.attack, self.defence)

    def display_pokemon(self):
        image = os.path.join(self.link_image, f"{self.name}.png")
        try:
            pokemon = pygame.image.load(image)
            print("Image loaded successfully!")
        except pygame.error as e:
            print(f"Error loading image: {e}")
            image = os.path.join(self.link_image, "default.png")
        return image

    def is_ko(self):
        if self.lifePoint <= 0:
            self.KO = True

    def record_pokemon(self):
        with open('pokemon.json', 'w') as fichier:
            json.dump(self.pokemon_list, fichier, indent=4)

    def get_pokemon_list(self):
        try:
            with open('pokemon.json', 'r') as fichier:
                pokemon_list = json.load(fichier)
        except FileNotFoundError:
            pokemon_list = []
        return pokemon_list

    def add_to_list(self, new_pokemon):
        new_pokemon_dict = new_pokemon.to_dict() if isinstance(new_pokemon, Pokemon) else new_pokemon
        if new_pokemon_dict not in self.pokemon_list:
            self.pokemon_list.append(new_pokemon_dict)
            self.record_pokemon()
        else:
            print('This Pokémon is already in your Pokédex.')

    def add_pokemon(self):
        # Création des champs de saisie
        input_boxes = [
            InputBox(800, 50, 200, 32),
            InputBox(800, 100, 200, 32),
            InputBox(800, 150, 200, 32),
            InputBox(800, 200, 200, 32),
            InputBox(800, 250, 200, 32),
            InputBox(800, 300, 200, 32),
            InputBox(800, 350, 200, 32)
        ]

        # Étiquettes pour les champs de saisie
        labels = [
            "Nom du Pokémon :",
            "Points de vie :",
            "Type principal :",
            "Type secondaire :",
            "Attaque :",
            "Défense :",
            "Points d'XP :"
        ]

        # Bouton pour ajouter un Pokémon
        add_button = pygame.Rect(800, 400, 200, 32)
        add_button_text = font.render("Ajouter", True, BLACK)

        # Boucle principale
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                for box in input_boxes:
                    box.handle_event(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if add_button.collidepoint(event.pos):
                        name = input_boxes[0].text
                        pv = int(input_boxes[1].text)
                        type1 = input_boxes[2].text
                        type2 = input_boxes[3].text if input_boxes[3].text else None
                        attack = int(input_boxes[4].text)
                        defense = int(input_boxes[5].text)
                        giveXP = int(input_boxes[6].text)
                        new_pokemon = Pokemon(
                            name=name,
                            lifePoint=pv,
                            level=1,
                            XP=0,
                            giveXP=giveXP,
                            limitXP=60,
                            attack=attack,
                            defence=defense,
                            type1=type1,
                            type2=type2,
                            next_evolution=None
                        )
                        self.add_to_list(new_pokemon)
                        print(f"{name} a été ajouté !")

            for box in input_boxes:
                box.update()

            screen.fill(WHITE)  # Remplit l'écran avec la couleur blanche
            for i, box in enumerate(input_boxes):
                box.draw(screen)
                label_surface = font.render(labels[i], True, BLACK)  # Couleur du texte en noir
                screen.blit(label_surface, (250, box.rect.y - 5))
            pygame.draw.rect(screen, YELLOW, add_button)
            screen.blit(add_button_text, (add_button.x + 5, add_button.y + 5))

            pygame.display.flip()

        pygame.quit()

    def to_dict(self):
        return {
            'name': self.name,
            'lifePoint': self.lifePoint,
            'level': self.level,
            'XP': self.experience,
            'giveXP': self.giveXp,
            'limitXP': self.limitXP,
            'attack': self.attack,
            'defence': self.defence,
            'type1': self.type1,
            'type2': self.type2,
            'KO': self.KO,
            'link_image': self.link_image,
            'statut': self.statut,
            'next_evolution': self.next_evolution.to_dict() if isinstance(self.next_evolution, Pokemon) else None
        }

    def level_up(self, opponent):
        if self.experience >= self.limitXP:
            self.level += 1
            self.limitXP *= 3
            self.experience = 0
            self.giveXp += 20
            self.lifePoint += 100
            self.attack += 25
            self.defence += 10
        elif self.experience < self.limitXP:
            self.experience += opponent.giveXp

        if self.level == 5:
            self.evolve(self.next_evolution)

    def __str__(self):
        return f"""
            name: {self.name}
            lifePoint: {self.lifePoint}
            level: {self.level}
            XP: {self.experience}
            giveXP: {self.giveXp}
            limitXP: {self.limitXP}
            attack: {self.attack}
            defence: {self.defence}
            type1: {self.type1}
            type2: {self.type2}
            next_evolution: {self.next_evolution}
        """

# Exemple d'utilisation
pikachu = Pokemon("pikachu", 100, 1, 0, 10, 20, 10, 8, "electric", None, None)
pikachu.add_pokemon()
