class Pokemon:
    def __init__(self, nom, lifePoint, level, XP, attack, defence, types, KO):
        self.nom = nom
        self.lifePoint = lifePoint
        self.level = level
        self.experience = XP
        self.attack = attack
        self.defence = defence
        self.type = types
        self.KO = KO

    def attack(self):
        print("attack")

    def display_pokemon(self):
        print("display pokemon")