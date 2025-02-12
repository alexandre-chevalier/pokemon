import random
import pygame
import os

class Pokemon:
    def __init__(self, name, lifePoint, level, XP, evolution, giveXP, limitXP,  attack, defence, type1, type2):
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
        self.KO = False
        self.link_image = "images"
        self.statut = "normal"

    def attacks(self, ennemyHp):
        coeff = 0.8
        damage = [self.attack, 0]
        coeffs = [coeff, 1-coeff]
        dmg = random.choices(damage, coeffs)
        ennemyHp.lifePoint -= dmg[0]
        if dmg[0] == 0:
            print("votre pokemon a louper son ataque")
        else:
            print(f"le pokemon adverse a perdu {self.attack} hp")

        return ennemyHp
        ## fonction subir degat
    def display_pokemon(self):
        image = os.path.join(super().display_pokemon() + f"\\{self.name}.png")
        try:
            pokemon = pygame.image.load(image)
            print("Image loaded successfully!")
        except pygame.error as e:
            print(f"Error loading image: {e}")

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

    def level_up(self):
        if self.experience >= self.limitXP:
            self.level +=1
            self.limitXP *= 3
            self.experience = 0
            self.giveXp +=20
            self.lifePoint  += 100
            self.attack     += 25
            self.defence    += 10

pikachu = Pokemon("Pikachu", 100, 1, 0, True, 10, 20,10, 8, "electric", None)
raichu = Pokemon("raichu", 120, 1 ,0 , True,60,120,30,25, "electric", None)
carapuce = Pokemon("carapuce", 120, 1, 0, True, 60, 120, 30, 25, "eau",None)
carabaffe = Pokemon("carabaffe", 175, 1, 0, True, 60, 120, 30, 25, "eau", None)
tortank = Pokemon("tortank", 250, 1, 0, False, 100, 120, 30,25, "eau", None)
salameche = Pokemon("salameche", 100, 1, 0, True, 60, 120, 30, 25, "feu", "terre")
reptincelle = Pokemon("reptincelle", 175, 1, 0, True, 60, 120, 30, 25, "feu", "terre")
dracaufeu = Pokemon("dracaufeu", 250, 1, 0, False, 100, 120, 30,25, "feu", None)
bulbizarre = Pokemon("bulbizarre", 100, 1, 0, True, 60, 120, 20, 25, "plante", "terre")
herbizarre = Pokemon("herbizarre", 175, 1,0, True, 60, 120, 30, 25, "plante", "terre")
florizarre = Pokemon("florizarre", 250, 1, 0, False, 100, 120, 30,25, "plante", "terre")
lugia = Pokemon("lugia", 175, 1,0, False, 100, 120, 30, 20,"vol", None)
artikodin = Pokemon("artikodin", 175, 1, 0, False, 60, 120, 30, 25, "vol", "glace")
taupiqueur = Pokemon("triopiqueur", 100, 1,0, True, 60, 120, 30, 25, "terre", None )
triopiqueur = Pokemon("triopiqueur",250,1, 0, False, 60,120,30,25, "terre", None)
rondoudou = Pokemon("rondoudou", 60, 1, 0, False, 60, 120, 50, 25, "normal", None)
grodoudou = Pokemon("grodoudou", 250, 1, 0, False, 60, 120, 30, 25, "normal", None)


print(pikachu.to_dict())