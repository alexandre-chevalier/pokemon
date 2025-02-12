import random
import pygame
import os


class Pokemon:
    def __init__(self, name, lifePoint, level, XP, evolution, giveXP, limitXP,  attack, defence, type1, type2, KO):
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
        self.link_image = r"C:\\Users\\alexc\\Desktop\\laplateforme\\projet\\annee1\\pokemon\\images"
        self.statut = "normal"

    def attacks(self, ennemyHp):

        ennemyHp -= self.attack
        print(f"le pokemon adverse a perdu {self.attack} hp")


    def is_ko(self):
        if self.lifePoint <= 0:
            self.KO = True
    
    def to_dict(self):
        dict_poke = {
                        "name": self.name,
                        "lifePoint": self.lifePoint,
                        "level": self.level,
                        "XP": self.experience,
                        "evolution": self.evolution,
                        "giveXp": self.giveXp,
                        "limitXp": self.limitXP,
                        "attack": self.attack,
                        "defence": self.defence,
                        "type1": self.type1,
                        "type2": self.type2,
                        "KO": self.KO,
                        "statut": self.statut
                    }
        return dict_poke

            
    def display_pokemon(self):
        image = self.link_image 
        
        return image

    def level_up(self, life_point_increase, attack_increase, defense_increase):
        if self.experience >= self.limitXP:
            self.level +=1
            self.limitXP *= 3
            self.experience = 0
            self.giveXp +=20
            self.lifePoint  += life_point_increase
            self.attack     += attack_increase
            self.defence    += defense_increase

## Create 20 subclass of pokemon, each subclass represent a pokemon
class Pikachu(Pokemon): 
    def __init__(self, lifePoint=100, level=1, XP=0, giveXP=10, limitXP=20, attack=10, defence=8, type1="electric", type2=None):
        super().__init__("Pikachu", lifePoint, level, XP, True, giveXP, limitXP, attack, defence, type1, type2, False)
    
    def to_dict(self):
        return super().to_dict()
    
    def display_pokemon(self):
        image = os.path.join(super().display_pokemon() + f"\\{self.name}.png")
        try:
            pokemon = pygame.image.load(image)
            print("Image loaded successfully!")
        except pygame.error as e:
            print(f"Error loading image: {e}")
            
    def level_ups(self):
        if self.experience >= self.limitXP and self.level == 1:
            super().level_up(20, 5, 4)
        elif self.experience >= self.limitXP and self.level == 2:
            super().level_up(20, 5, 4)
        elif self.experience >= self.limitXP and self.level == 3:
            super().level_up(30, 5, 4)
        elif self.experience >= self.limitXP and self.level == 4:
            super().level_up(40, 5, 4)
        elif self.experience >= self.limitXP and self.level == 5:
            super().level_up(60, 5, 4)

class Raichu(Pokemon):
    def __init__(self, lifePoint=250, level=1, XP=0, giveXP=60, limitXP=120, attack=30, defence=25, type1="electric", type2=None ):
        super().__init__("Raichu", lifePoint, level, XP, False, giveXP, limitXP, attack, defence, type1, type2, False)

    def to_dict(self):
        return super().to_dict()
    
    def display_pokemon(self):
        image = os.path.join(super().display_pokemon() + f"\\{self.name}.png")
        try:
            pokemon = pygame.image.load(image)
            print("Image loaded successfully!")
        except pygame.error as e:
            print(f"Error loading image: {e}")
        
    
    def level_ups(self):
        if self.experience > self.limitXP and self.level == 1:
            super().level_up(20, 5, 4)
        elif self.experience > self.limitXP and self.level == 2:
            super().level_up(40, 10, 8)
        elif self.experience > self.limitXP and self.level == 3:
            super().level_up(50, 20, 8)
        elif self.experience > self.limitXP and self.level == 4:
            super().level_up(60, 30, 12)
        elif self.experience > self.limitXP and self.level == 5:
            super().level_up(60, 30, 15)

class Carapuce(Pokemon):
    def __init__(self, lifePoint=250, level=1, XP=0, giveXP=60, limitXP=120, attack=30, defence=25, type1="eau", type2=None ):
        super().__init__("carapuce", lifePoint, level, XP, True, giveXP, limitXP, attack, defence, type1, type2, False)
    
    def to_dict(self):
        return super().to_dict()
    
    def display_pokemon(self):
        image = os.path.join(super().display_pokemon() + f"\\{self.name}.png")
        try:
            pokemon = pygame.image.load(image)
            print("Image loaded successfully!")
        except pygame.error as e:
            print(f"Error loading image: {e}")
    
    def level_ups(self):
        if self.experience > self.limitXP and self.level == 1:
            super().level_up(20, 5, 4)
        elif self.experience > self.limitXP and self.level == 2:
            super().level_up(40, 10, 8)
        elif self.experience > self.limitXP and self.level == 3:
            super().level_up(50, 20, 8)
        elif self.experience > self.limitXP and self.level == 4:
            super().level_up(60, 30, 12)
        elif self.experience > self.limitXP and self.level == 5:
            super().level_up(60, 30, 15)

class Carabaffe(Pokemon):
    def __init__(self, lifePoint=250, level=1, XP=0, giveXP=60, limitXP=120, attack=30, defence=25, type1="eau", type2=None ):
        super().__init__("carabaffe", lifePoint, level, XP, True, giveXP, limitXP, attack, defence, type1, type2, False)

    def to_dict(self):
        return super().to_dict()
    
    def display_pokemon(self):
        image = os.path.join(super().display_pokemon() + f"\\{self.name}.png")
        try:
            pokemon = pygame.image.load(image)
            print("Image loaded successfully!")
        except pygame.error as e:
            print(f"Error loading image: {e}")
    
    def level_ups(self):
        if self.experience > self.limitXP and self.level == 1:
            super().level_up(20, 5, 4)
        elif self.experience > self.limitXP and self.level == 2:
            super().level_up(40, 10, 8)
        elif self.experience > self.limitXP and self.level == 3:
            super().level_up(50, 20, 8)
        elif self.experience > self.limitXP and self.level == 4:
            super().level_up(60, 30, 12)
        elif self.experience > self.limitXP and self.level == 5:
            super().level_up(60, 30, 15)

class Tortank(Pokemon):
    def __init__(self, lifePoint=250, level=1, XP=0, giveXP=60, limitXP=120, attack=30, defence=25, type1="eau", type2=None ):
        super().__init__("tortank", lifePoint, level, XP, False, giveXP, limitXP, attack, defence, type1, type2, False)

    def to_dict(self):
        return super().to_dict()
    
    def display_pokemon(self):
        image = os.path.join(super().display_pokemon() + f"\\{self.name}.png")
        try:
            pokemon = pygame.image.load(image)
            print("Image loaded successfully!")
        except pygame.error as e:
            print(f"Error loading image: {e}")
    
    def level_ups(self):
        if self.experience > self.limitXP and self.level == 1:
            super().level_up(20, 5, 4)
        elif self.experience > self.limitXP and self.level == 2:
            super().level_up(40, 10, 8)
        elif self.experience > self.limitXP and self.level == 3:
            super().level_up(50, 20, 8)
        elif self.experience > self.limitXP and self.level == 4:
            super().level_up(60, 30, 12)
        elif self.experience > self.limitXP and self.level == 5:
            super().level_up(60, 30, 15)

class Salameche(Pokemon):
    def __init__(self, lifePoint=250, level=1, XP=0, giveXP=60, limitXP=120, attack=30, defence=25, type1="feu", type2="terre" ):
        super().__init__("salameche", lifePoint, level, XP, True, giveXP, limitXP, attack, defence, type1, type2, False)

    def to_dict(self):
        return super().to_dict()
    
    def display_pokemon(self):
        image = os.path.join(super().display_pokemon() + f"\\{self.name}.png")
        try:
            pokemon = pygame.image.load(image)
            print("Image loaded successfully!")
        except pygame.error as e:
            print(f"Error loading image: {e}")
    
    def level_ups(self):
        if self.experience > self.limitXP and self.level == 1:
            super().level_up(20, 5, 4)
        elif self.experience > self.limitXP and self.level == 2:
            super().level_up(40, 10, 8)
        elif self.experience > self.limitXP and self.level == 3:
            super().level_up(50, 20, 8)
        elif self.experience > self.limitXP and self.level == 4:
            super().level_up(60, 30, 12)
        elif self.experience > self.limitXP and self.level == 5:
            super().level_up(60, 30, 15)

class Reptincelle(Pokemon):
    def __init__(self, lifePoint=250, level=1, XP=0, giveXP=60, limitXP=120, attack=30, defence=25, type1="feu", type2="terre" ):
        super().__init__("reptincelle", lifePoint, level, XP, True, giveXP, limitXP, attack, defence, type1, type2, False)
    
    def to_dict(self):
        return super().to_dict()
    
    def display_pokemon(self):
        image = os.path.join(super().display_pokemon() + f"\\{self.name}.png")
        try:
            pokemon = pygame.image.load(image)
            print("Image loaded successfully!")
        except pygame.error as e:
            print(f"Error loading image: {e}")
    
    def level_ups(self):
        if self.experience > self.limitXP and self.level == 1:
            super().level_up(20, 5, 4)
        elif self.experience > self.limitXP and self.level == 2:
            super().level_up(40, 10, 8)
        elif self.experience > self.limitXP and self.level == 3:
            super().level_up(50, 20, 8)
        elif self.experience > self.limitXP and self.level == 4:
            super().level_up(60, 30, 12)
        elif self.experience > self.limitXP and self.level == 5:
            super().level_up(60, 30, 15)


class Dracaufeu(Pokemon):
    def __init__(self, lifePoint=250, level=1, XP=0, giveXP=60, limitXP=120, attack=30, defence=25, type1="feu", type2="vol" ):
        super().__init__("dracaufeu", lifePoint, level, XP, False, giveXP, limitXP, attack, defence, type1, type2, False)
    
    def to_dict(self):
        return super().to_dict()
    
    def display_pokemon(self):
        image = os.path.join(super().display_pokemon() + f"\\{self.name}.png")
        try:
            pokemon = pygame.image.load(image)
            print("Image loaded successfully!")
        except pygame.error as e:
            print(f"Error loading image: {e}")
    
    def level_ups(self):
        if self.experience > self.limitXP and self.level == 1:
            super().level_up(20, 5, 4)
        elif self.experience > self.limitXP and self.level == 2:
            super().level_up(40, 10, 8)
        elif self.experience > self.limitXP and self.level == 3:
            super().level_up(50, 20, 8)
        elif self.experience > self.limitXP and self.level == 4:
            super().level_up(60, 30, 12)
        elif self.experience > self.limitXP and self.level == 5:
            super().level_up(60, 30, 15)


class Bulbizarre(Pokemon):
    def __init__(self, lifePoint=250, level=1, XP=0, giveXP=60, limitXP=120, attack=30, defence=25, type1="plante", type2="terre" ):
        super().__init__("bulbizarre", lifePoint, level, XP, True, giveXP, limitXP, attack, defence, type1, type2, False)

    def to_dict(self):
        return super().to_dict()
    
    def display_pokemon(self):
        image = os.path.join(super().display_pokemon() + f"\\{self.name}.png")
        try:
            pokemon = pygame.image.load(image)
            print("Image loaded successfully!")
        except pygame.error as e:
            print(f"Error loading image: {e}")
    
    def level_ups(self):
        if self.experience > self.limitXP and self.level == 1:
            super().level_up(20, 5, 4)
        elif self.experience > self.limitXP and self.level == 2:
            super().level_up(40, 10, 8)
        elif self.experience > self.limitXP and self.level == 3:
            super().level_up(50, 20, 8)
        elif self.experience > self.limitXP and self.level == 4:
            super().level_up(60, 30, 12)
        elif self.experience > self.limitXP and self.level == 5:
            super().level_up(60, 30, 15)



class Herbizarre(Pokemon):
    def __init__(self, lifePoint=250, level=1, XP=0, giveXP=60, limitXP=120, attack=30, defence=25, type1="plante", type2="terre" ):
        super().__init__("herbizarre", lifePoint, level, XP, True, giveXP, limitXP, attack, defence, type1, type2, False)
    
    def to_dict(self):
        return super().to_dict()
        
    def display_pokemon(self):
        image = os.path.join(super().display_pokemon() + f"\\{self.name}.png")
        try:
            pokemon = pygame.image.load(image)
            print("Image loaded successfully!")
        except pygame.error as e:
            print(f"Error loading image: {e}")
    
    def level_ups(self):
        if self.experience > self.limitXP and self.level == 1:
            super().level_up(20, 5, 4)
        elif self.experience > self.limitXP and self.level == 2:
            super().level_up(40, 10, 8)
        elif self.experience > self.limitXP and self.level == 3:
            super().level_up(50, 20, 8)
        elif self.experience > self.limitXP and self.level == 4:
            super().level_up(60, 30, 12)
        elif self.experience > self.limitXP and self.level == 5:
            super().level_up(60, 30, 15)


class Florizare(Pokemon):
    def __init__(self, lifePoint=250, level=1, XP=0, giveXP=60, limitXP=120, attack=30, defence=25, type1="plante", type2="terre" ):
        super().__init__("florizarre", lifePoint, level, XP, False, giveXP, limitXP, attack, defence, type1, type2, False)

    def to_dict(self):
        return super().to_dict()
    
    def display_pokemon(self):
        image = os.path.join(super().display_pokemon() + f"\\{self.name}.png")
        try:
            pokemon = pygame.image.load(image)
            print("Image loaded successfully!")
        except pygame.error as e:
            print(f"Error loading image: {e}")
    
    def level_ups(self):
        if self.experience > self.limitXP and self.level == 1:
            super().level_up(20, 5, 4)
        elif self.experience > self.limitXP and self.level == 2:
            super().level_up(40, 10, 8)
        elif self.experience > self.limitXP and self.level == 3:
            super().level_up(50, 20, 8)
        elif self.experience > self.limitXP and self.level == 4:
            super().level_up(60, 30, 12)
        elif self.experience > self.limitXP and self.level == 5:
            super().level_up(60, 30, 15)


class Lugia(Pokemon):
    def __init__(self, lifePoint=150, level=1, XP=0, giveXP=60, limitXP=120, attack=30, defence=20, type1="vol", type2=None ):
        super().__init__("lugia", lifePoint, level, XP, False, giveXP, limitXP, attack, defence, type1, type2, False)

    def to_dict(self):
        return super().to_dict()
    
    def display_pokemon(self):
        image = os.path.join(super().display_pokemon() + f"\\{self.name}.png")
        try:
            pokemon = pygame.image.load(image)
            print("Image loaded successfully!")
        except pygame.error as e:
            print(f"Error loading image: {e}")
    
    def level_ups(self):
        if self.experience > self.limitXP and self.level == 1:
            super().level_up(20, 5, 4)
        elif self.experience > self.limitXP and self.level == 2:
            super().level_up(40, 10, 8)
        elif self.experience > self.limitXP and self.level == 3:
            super().level_up(50, 20, 8)
        elif self.experience > self.limitXP and self.level == 4:
            super().level_up(60, 30, 12)
        elif self.experience > self.limitXP and self.level == 5:
            super().level_up(60, 30, 15)

class Artikodin(Pokemon):
    def __init__(self, lifePoint=175, level=1, XP=0, giveXP=120, limitXP=120, attack=30, defence=25, type1="vol", type2="glace" ):
        super().__init__("artikodin", lifePoint, level, XP, False, giveXP, limitXP, attack, defence, type1, type2, False)

    def to_dict(self):
        return super().to_dict()
    
    def display_pokemon(self):
        image = os.path.join(super().display_pokemon() + f"\\{self.name}.png")
        try:
            pokemon = pygame.image.load(image)
            print("Image loaded successfully!")
        except pygame.error as e:
            print(f"Error loading image: {e}")
    
    def level_ups(self):
        if self.experience > self.limitXP and self.level == 1:
            super().level_up(40, 5, 4)
        elif self.experience > self.limitXP and self.level == 2:
            super().level_up(40, 10, 8)
        elif self.experience > self.limitXP and self.level == 3:
            super().level_up(50, 20, 8)
        elif self.experience > self.limitXP and self.level == 4:
            super().level_up(60, 30, 12)
        elif self.experience > self.limitXP and self.level == 5:
            super().level_up(60, 30, 15)

class Taupiqueur(Pokemon):
    def __init__(self, lifePoint=100, level=1, XP=0, giveXP=60, limitXP=120, attack=30, defence=25, type1="terre", type2=None ):
        super().__init__("taupiqueur", lifePoint, level, XP, True, giveXP, limitXP, attack, defence, type1, type2, False)

    def to_dict(self):
        return super().to_dict()
    
    def display_pokemon(self):
        image = os.path.join(super().display_pokemon() + f"\\{self.name}.png")
        try:
            pokemon = pygame.image.load(image)
            print("Image loaded successfully!")
        except pygame.error as e:
            print(f"Error loading image: {e}")
    
    def level_ups(self):
        if self.experience > self.limitXP and self.level == 1:
            super().level_up(20, 5, 4)
        elif self.experience > self.limitXP and self.level == 2:
            super().level_up(40, 10, 8)
        elif self.experience > self.limitXP and self.level == 3:
            super().level_up(50, 20, 8)
        elif self.experience > self.limitXP and self.level == 4:
            super().level_up(60, 30, 12)
        elif self.experience > self.limitXP and self.level == 5:
            super().level_up(60, 30, 15)

class Triopiqueur(Pokemon):
    def __init__(self, lifePoint=250, level=1, XP=0, giveXP=60, limitXP=120, attack=30, defence=25, type1="terre", type2=None ):
        super().__init__("triopiqueur", lifePoint, level, XP, False, giveXP, limitXP, attack, defence, type1, type2, False)
    
    def to_dict(self):
        return super().to_dict()
    
    def display_pokemon(self):
        image = os.path.join(super().display_pokemon() + f"\\{self.name}.png")
        try:
            pokemon = pygame.image.load(image)
            print("Image loaded successfully!")
        except pygame.error as e:
            print(f"Error loading image: {e}")
    
    def level_ups(self):
        if self.experience > self.limitXP and self.level == 1:
            super().level_up(20, 5, 4)
        elif self.experience > self.limitXP and self.level == 2:
            super().level_up(40, 10, 8)
        elif self.experience > self.limitXP and self.level == 3:
            super().level_up(50, 20, 8)
        elif self.experience > self.limitXP and self.level == 4:
            super().level_up(60, 30, 12)
        elif self.experience > self.limitXP and self.level == 5:
            super().level_up(60, 30, 15)

class Rondoudou(Pokemon):
    def __init__(self, lifePoint=60, level=1, XP=0, giveXP=60, limitXP=120, attack=50, defence=25, type1="normal", type2=None ):
        super().__init__("rondoudou", lifePoint, level, XP, False, giveXP, limitXP, attack, defence, type1, type2, False)

    def to_dict(self):
        return super().to_dict()
    
    def display_pokemon(self):
        image = os.path.join(super().display_pokemon() + f"\\{self.name}.png")
        try:
            pokemon = pygame.image.load(image)
            print("Image loaded successfully!")
        except pygame.error as e:
            print(f"Error loading image: {e}")
    
    def level_ups(self):
        if self.experience > self.limitXP and self.level == 1:
            super().level_up(20, 5, 4)
        elif self.experience > self.limitXP and self.level == 2:
            super().level_up(40, 10, 8)
        elif self.experience > self.limitXP and self.level == 3:
            super().level_up(50, 20, 8)
        elif self.experience > self.limitXP and self.level == 4:
            super().level_up(60, 30, 12)
        elif self.experience > self.limitXP and self.level == 5:
            super().level_up(60, 30, 15)

class Grodoudou(Pokemon):
    def __init__(self, lifePoint=250, level=1, XP=0, giveXP=60, limitXP=120, attack=30, defence=25, type1="normal", type2=None):
        super().__init__("grodoudou", lifePoint, level, XP, False, giveXP, limitXP, attack, defence, type1, type2, False)

    def to_dict(self):
        return super().to_dict()
    
    def display_pokemon(self):
        image = os.path.join(super().display_pokemon() + f"\\{self.name}.png")
        try:
            pokemon = pygame.image.load(image)
            print("Image loaded successfully!")
        except pygame.error as e:
            print(f"Error loading image: {e}")
    
    def level_ups(self):
        if self.experience > self.limitXP and self.level == 1:
            super().level_up(20, 5, 4)
        elif self.experience > self.limitXP and self.level == 2:
            super().level_up(40, 10, 8)
        elif self.experience > self.limitXP and self.level == 3:
            super().level_up(50, 20, 8)
        elif self.experience > self.limitXP and self.level == 4:
            super().level_up(60, 30, 12)
        elif self.experience > self.limitXP and self.level == 5:
            super().level_up(60, 30, 15)


pikachu = Pikachu()

print(pikachu.to_dict())
