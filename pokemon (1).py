import pygame

class Pokemon:
    def __init__(self, name, lifePoint, level, XP, evolution, giveXP, limitXP, attack, defence, type1, type2, KO, image_path="images/default.png", x=0, y=0):
        """Initialisation d'un Pokémon avec une image et une position"""
        self.name = name
        self.lifePoint = lifePoint
        self.level = level
        self.experience = XP
        self.evolution = evolution
        self.giveXp = giveXP
        self.limitXP = limitXP
        self.attack = attack
        self.defence = defence
        self.type1 = type1
        self.type2 = type2
        self.KO = KO

        # 🔹 Chargement et redimensionnement de l’image
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (50, 50))

        # 🔹 Création d’un rectangle pour positionner le Pokémon
        self.rect = self.image.get_rect(topleft=(x, y))

    def display(self, screen):
        """Affiche le Pokémon à sa position"""
        screen.blit(self.image, self.rect.topleft)

    def level_up(self, life_point_increase, attack_increase, defense_increase):
        """Système d'évolution unique pour tous les Pokémon"""
        if self.experience >= self.limitXP:
            self.level += 1
            self.limitXP *= 3
            self.experience = 0
            self.lifePoint += life_point_increase
            self.attack += attack_increase
            self.defence += defense_increase

    def level_ups(self):
        """Méthode d'évolution basée sur le niveau"""
        stats = [(20, 5, 4), (40, 10, 8), (50, 20, 8), (60, 30, 12), (60, 30, 15)]
        if self.level <= 5 and self.experience >= self.limitXP:
            self.level_up(*stats[self.level - 1])

# 🔹 Liste des Pokémon avec héritage optimisé
class Pikachu(Pokemon):
    def __init__(self, x=0, y=0):
        super().__init__("Pikachu", 100, 1, 0, True, 10, 20, 10, 8, "electric", None, False, "images/pikachu.png", x, y)

class Dracaufeu(Pokemon):
    def __init__(self, x=0, y=0):
        super().__init__("Dracaufeu", 250, 1, 0, False, 60, 120, 30, 25, "fire", "flying", False, "images/dracaufeu.png", x, y)

class Carapuce(Pokemon):
    def __init__(self, x=0, y=0):
        super().__init__("Carapuce", 250, 1, 0, True, 60, 120, 30, 25, "water", None, False, "images/carapuce.png", x, y)

class Carabaffe(Pokemon):
    def __init__(self, x=0, y=0):
        super().__init__("Carabaffe", 300, 1, 0, True, 70, 150, 35, 30, "water", None, False, "images/carabaffe.png", x, y)

class Tortank(Pokemon):
    def __init__(self, x=0, y=0):
        super().__init__("Tortank", 400, 1, 0, False, 80, 180, 45, 40, "water", None, False, "images/tortank.png", x, y)

class Salameche(Pokemon):
    def __init__(self, x=0, y=0):
        super().__init__("Salameche", 200, 1, 0, True, 50, 100, 25, 20, "fire", None, False, "images/salameche.png", x, y)

class Reptincelle(Pokemon):
    def __init__(self, x=0, y=0):
        super().__init__("Reptincelle", 250, 1, 0, True, 60, 120, 30, 25, "fire", None, False, "images/reptincelle.png", x, y)

class Bulbizarre(Pokemon):
    def __init__(self, x=0, y=0):
        super().__init__("Bulbizarre", 220, 1, 0, True, 55, 110, 28, 22, "grass", "poison", False, "images/bulbizarre.png", x, y)

class Herbizarre(Pokemon):
    def __init__(self, x=0, y=0):
        super().__init__("Herbizarre", 270, 1, 0, True, 65, 130, 33, 27, "grass", "poison", False, "images/herbizarre.png", x, y)

class Florizarre(Pokemon):
    def __init__(self, x=0, y=0):
        super().__init__("Florizarre", 350, 1, 0, False, 75, 160, 40, 35, "grass", "poison", False, "images/florizarre.png", x, y)

# Ajout d'un dictionnaire pour stocker tous les Pokémon
POKEMONS = {
    "Pikachu": Pikachu,
    "Dracaufeu": Dracaufeu,
    "Carapuce": Carapuce,
    "Carabaffe": Carabaffe,
    "Tortank": Tortank,
    "Salameche": Salameche,
    "Reptincelle": Reptincelle,
    "Bulbizarre": Bulbizarre,
    "Herbizarre": Herbizarre,
    "Florizarre": Florizarre,
}
