import pygame
import os

class Pokemon:
    def __init__(self, name, lifePoint, level, XP, giveXP, limitXP,  attack, defence, type1, type2, next_evolution):
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

    

    def evolve(self, pokemon):
        if pokemon:
            self.name = pokemon.name
            self.lifePoint = pokemon.lifePoint
            self.level = pokemon.level
            self.experience = pokemon.experience
            self.giveXp =  pokemon.giveXp
            self.limitXP = pokemon.limitXP
            self.attack = pokemon.attack
            self.defence = pokemon.defence
            self.type1 = pokemon.type1
            self.type2 = pokemon.type2
            self.next_evolution = pokemon.next_evolution


    def attacks(self):
        return (self.attack, self.defence)

    def display_pokemon(self):
        try:
            image = os.path.join(self.link_image + f"{self.name}.png")
        except FileNotFoundError:
            image = os.path.join(self.link_image + "default.png")
        try:
            pokemon = pygame.image.load(image)
            print("Image loaded successfully!")
        except pygame.error as e:
            print(f"Error loading image: {e}")
        return image

    def is_ko(self):
        if self.lifePoint <= 0:
            self.KO = True
    
    def to_dict(self):
        return {
            'name': self.name,
            'lifePoint': self.lifePoint,
            'level': self.level,
            'experience': self.experience,
            'giveXp': self.giveXp,
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
            self.level +=1
            self.limitXP *= 3
            self.experience = 0
            self.giveXp +=20
            self.lifePoint  += 100
            self.attack     += 25
            self.defence    += 10
        elif self.experience < self.limitXP:
            self.experience += opponent.giveXp

        if self.level == 5:
            self.evolve(self.next_evolution)
    
    def __str__(self):
            return f"""
                name : {self.name}
                lifepoint : {self.lifePoint}
                level : {self.level}
                xp : {self.experience}
                giveXp : {self.giveXp}
                limitXp : {self.limitXP}
                attack : {self.attack}
                defence : {self.defence}
                type1 : {self.type1}
                type2 : {self.type2}
                next_evolution : {self.next_evolution}
                """

raichu = Pokemon("raichu", 250, 1, 0, 100, 120, 30,25, "electric", None, None)
pikachu = Pokemon("Pikachu", 100, 1, 0, 10, 20,10, 8, "electric", None, raichu)
tortank = Pokemon("tortank", 250, 1, 0, 100, 120, 30,25, "eau", None, None)
carabaffe = Pokemon("carabaffe", 175, 1, 0, 60, 120, 30, 25, "eau", None, tortank)
carapuce = Pokemon("carapuce", 120, 1, 0,60, 120, 30, 25, "eau",None, carabaffe)
dracaufeu = Pokemon("dracaufeu", 250, 1, 0, 100, 120, 30,25, "feu", None, None)
reptincelle = Pokemon("reptincelle", 175, 1, 0, 60, 120, 30, 25, "feu", "terre",dracaufeu)
salameche = Pokemon("salameche", 100, 1, 0,60, 120, 30, 25, "feu", "terre",reptincelle)
florizarre = Pokemon("florizarre", 250, 1, 0,100, 120, 30,25, "plante", "terre", None)
herbizarre = Pokemon("herbizarre", 175, 1,0,  60, 120, 30, 25, "plante", "terre",florizarre)
bulbizarre = Pokemon("bulbizarre", 100, 1, 0, 60, 120, 20, 25, "plante", "terre",herbizarre)
lugia = Pokemon("lugia", 175, 1,0, 100, 120, 30, 20,"vol", None, None)
artikodin = Pokemon("artikodin", 175, 1, 0, 60, 120, 30, 25, "vol", "glace", None)
triopiqueur = Pokemon("triopiqueur",250,1, 0, 60,120,30,25, "terre", None, None)
taupiqueur = Pokemon("triopiqueur", 100, 1,0, 60, 120, 30, 25, "terre", None,triopiqueur )
grodoudou = Pokemon("grodoudou", 250, 1, 0, 60, 120, 30, 25, "normal", None,None)
rondoudou = Pokemon("rondoudou", 60, 1, 0, 60, 120, 50, 25, "normal", None,grodoudou)
grotadmorv = Pokemon("grotadmorv", 175, 1,0, 100, 120, 30, 20,"poison", None, None)
tadmorv = Pokemon("tadmorv", 120, 1,0, 100, 120, 30, 20,"poison", None, grotadmorv)
ronflex = Pokemon("triopiqueur",250,1, 0, 60,120,30,25, "terre", None, None)
hoho = Pokemon("hoho", 200, 1,0, 100, 120, 30, 20,"vol", "feu", None)
