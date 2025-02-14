import pygame
import os

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
        self.link_image = f"images/{name}.png"
        self.statut = "normal"
        self.next_evolution = next_evolution

    

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

<<<<<<< HEAD
    def attacks(self, ennemyHp):
        coeff = 0.8
        damage = [self.attack, 0]
        coeffs = [coeff, 1 - coeff]
        dmg = random.choices(damage, coeffs)
        ennemyHp.lifePoint -= dmg[0]
        if dmg[0] == 0:
            print("votre pokemon a louper son attaque")
        else:
            print(f"le pokemon adverse a perdu {self.attack} hp")

        return ennemyHp

=======

    def attacks(self):
        return (self.attack, self.defence)

>>>>>>> origin/alexandre
    def display_pokemon(self):
        try:
            image = os.path.join(self.link_image)
        except FileNotFoundError:
<<<<<<< HEAD
            image = os.path.join("images/default.png")

        print(image)
=======
            image = os.path.join(self.link_image + "default.png")
>>>>>>> origin/alexandre
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

<<<<<<< HEAD
    def level_up(self):
=======
    def level_up(self, opponent):
>>>>>>> origin/alexandre
        if self.experience >= self.limitXP:
            self.level += 1
            self.limitXP *= 3
            self.experience = 0
<<<<<<< HEAD
            self.giveXp += 20
            self.lifePoint += 100
            self.attack += 25
            self.defence += 10
=======
            self.giveXp +=20
            self.lifePoint  += 100
            self.attack     += 25
            self.defence    += 10
        elif self.experience < self.limitXP:
            self.experience += opponent.giveXp
>>>>>>> origin/alexandre

        if self.level == 5:
            self.evolve(self.next_evolution)

    def __str__(self):
<<<<<<< HEAD
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

# Define Pokémon instances
raichu = Pokemon("Raichu", 250, 1, 0, 100, 120, 30, 25, "electric", None, None)
pikachu = Pokemon("Pikachu", 100, 1, 0, 10, 20, 10, 8, "electric", None, raichu)
tortank = Pokemon("Tortank", 250, 1, 0, 100, 120, 30, 25, "eau", None, None)
carabaffe = Pokemon("Carabaffe", 175, 1, 0, 60, 120, 30, 25, "eau", None, tortank)
carapuce = Pokemon("Carapuce", 120, 1, 0, 60, 120, 30, 25, "eau", None, carabaffe)
dracaufeu = Pokemon("Dracaufeu", 250, 1, 0, 100, 120, 30, 25, "feu", None, None)
reptincelle = Pokemon("Reptincelle", 175, 1, 0, 60, 120, 30, 25, "feu", "terre", dracaufeu)
salameche = Pokemon("Salameche", 100, 1, 0, 60, 120, 30, 25, "feu", "terre", reptincelle)
florizarre = Pokemon("Florizarre", 250, 1, 0, 100, 120, 30, 25, "plante", "terre", None)
herbizarre = Pokemon("Herbizarre", 175, 1, 0, 60, 120, 30, 25, "plante", "terre", florizarre)
bulbizarre = Pokemon("Bulbizarre", 100, 1, 0, 60, 120, 20, 25, "plante", "terre", herbizarre)
lugia = Pokemon("Lugia", 175, 1, 0, 100, 120, 30, 20, "vol", None, None)
artikodin = Pokemon("Artikodin", 175, 1, 0, 60, 120, 30, 25, "vol", "glace", None)
triopiqueur = Pokemon("Triopiqueur", 250, 1, 0, 60, 120, 30, 25, "terre", None, None)
taupiqueur = Pokemon("Taupiqueur", 100, 1, 0, 60, 120, 30, 25, "terre", None, triopiqueur)
grodoudou = Pokemon("Grodoudou", 250, 1, 0, 60, 120, 30, 25, "normal", None, None)
rondoudou = Pokemon("Rondoudou", 60, 1, 0, 60, 120, 50, 25, "normal", None, grodoudou)
grotadmorv = Pokemon("Grotadmorv", 175, 1, 0, 100, 120, 30, 20, "vol", None, None)
tadmorv = Pokemon("Tadmorv", 120, 1, 0, 100, 120, 30, 20, "poison", None, grotadmorv)
ronflex = Pokemon("Ronflex", 250, 1, 0, 60, 120, 30, 25, "normal", None, None)
hoho = Pokemon("Hoho", 200, 1, 0, 100, 120, 30, 20, "vol", "feu", None)

print(rondoudou.to_dict())

rondoudou.level = 5
rondoudou.level_up()
print(rondoudou.to_dict())
=======
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
>>>>>>> origin/alexandre
