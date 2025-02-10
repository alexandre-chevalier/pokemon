class Pokemon:
    def __init__(self, name, lifePoint, level, XP, evolution,  attack, defence, type1, type2, KO):
        self.name = name
        self.lifePoint = lifePoint
        self.level = level
        self.experience = XP
        self.evolution = evolution
        self.attack = attack
        self.defence = defence
        self.type1 = type1
        self.type2 = type2
        self.KO = KO

    def attacks(self):
        print("attack")

    def display_pokemon(self):
        print("display pokemon")

## Create 20 subclass of pokemon, each subclass represent a pokemon
class Pikachu(Pokemon):
    def __init__(self, name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO):
        super().__init__(name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO)
        

    def evolution(self):
        print("pikachu evolve into raichu")

    def levels(self):
        print("level condition to change the basic state")



class Raichu(Pokemon):
    def __init__(self, name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO):
        super().__init__(name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO)

    def evolution(self):
        print("condition to evolve is to have an evolution")

    def levels(self):
        print("level condition to change the basic state")



class Lugia(Pokemon):
    def __init__(self, name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO):
        super().__init__(name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO)

    def evolution(self):
        print("cannot evolve")

    def levels(self):
        print("level condition to change the basic state")



class Bulbizarre(Pokemon):
    def __init__(self, name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO):
        super().__init__(name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO)

    def evolution(self):
        print("pikachu evolve into raichu")

    def levels(self):
        print("level condition to change the basic state")



class Herbizarre(Pokemon):
    def __init__(self, name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO):
        super().__init__(name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO)

    def evolution(self):
        print("pikachu evolve into raichu")

    def levels(self):
        print("level condition to change the basic state")



class Florizarre(Pokemon):
    def __init__(self, name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO):
        super().__init__(name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO)

    def evolution(self):
        print("pikachu evolve into raichu")

    def levels(self):
        print("level condition to change the basic state")


class Salameche(Pokemon):
    def __init__(self, name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO):
        super().__init__(name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO)

    def evolution(self):
        print("salameche evolve into reptincelle")

    def levels(self):
        print("level condition to change the basic state")   


class Reptincelle(Pokemon):
    def __init__(self, name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO):
        super().__init__(name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO)
        

    def evolution(self):
        print("reptincelle evolve into dracaufeu")

    def levels(self):
        print("level condition to change the basic state")    


class Dracaufeu(Pokemon):
    def __init__(self, name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO):
        super().__init__(name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO)

    def evolution(self):
        print("salameche evolve into reptincelle")

    def levels(self):
        print("level condition to change the basic state")   



class Roucool(Pokemon):
    def __init__(self, name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO):
        super().__init__(name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO)

    def evolution(self):
        print("roucool evolve into roucoups")

    def levels(self):
        print("level condition to change the basic state")   



class Roucoups(Pokemon):
    def __init__(self, name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO):
        super().__init__(name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO)

    def evolution(self):
        print("roucoups evolve into roucarnage")

    def levels(self):
        print("level condition to change the basic state") 


class Roucarnage(Pokemon):
    def __init__(self, name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO):
        super().__init__(name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO)

    def evolution(self):
        print("roucarnage cannot evolve")

    def levels(self):
        print("level condition to change the basic state")     



class Carapuce(Pokemon):
    def __init__(self, name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO):
        super().__init__(name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO)

    def evolution(self):
        print("carapuce evolve into carabaffe")

    def levels(self):
        print("level condition to change the basic state")


class Carabaffe(Pokemon):
    def __init__(self, name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO):
        super().__init__(name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO)

    def evolution(self):
        print("carapuce evolve into tortank")

    def levels(self):
        print("level condition to change the basic state")   


class Tortank(Pokemon):
    def __init__(self, name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO):
        super().__init__(name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO)

    def evolution(self):
        print("tortank cannot evolve")

    def levels(self):
        print("level condition to change the basic state")   


class Artikodin(Pokemon):
    def __init__(self, name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO):
        super().__init__(name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO)

    def evolution(self):
        print("artikodin cannot evolve")

    def levels(self):
        print("level condition to change the basic state") 

class Taupiqueur(Pokemon):
    def __init__(self, name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO):
        super().__init__(name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO)

    def evolution(self):
        print("taupiqueur evolve into triopiqueur")

    def levels(self):
        print("level condition to change the basic state")


class Triopiqueur(Pokemon):
    def __init__(self, name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO):
        super().__init__(name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO)

    def evolution(self):
        print("triopiqueur cannot evolve")

    def levels(self):
        print("level condition to change the basic state") 


class Rondoudou(Pokemon):
    def __init__(self, name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO):
        super().__init__(name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO)

    def evolution(self):
        print("rondoudou evolve into grosdoudou")

    def levels(self):
        print("level condition to change the basic state")


class Grosdoudou(Pokemon):
    def __init__(self, name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO):
        super().__init__(name, lifePoint, level, XP, evolution, attack, defence, type1, type2, KO)

    def evolution(self):
        print("grosdoudou cannot evolve")

    def levels(self):
        print("level condition to change the basic state")    