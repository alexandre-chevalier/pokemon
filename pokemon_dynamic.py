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
