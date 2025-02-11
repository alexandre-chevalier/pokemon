import json

# entries structures => "pokemon" : {"name" : "", "lifepoint": 10,"level": 1, "experience": 0, "attack": 1, "defense" : 1, "type": ""}
class Pokemon_bank:
    def __init__ (self, name):
        self.name = name
        self.pokemon_list = []

#Record entry in pokemon.json
    def record_pokemon(self):
        with open('pokemon.json', 'w') as fichier:
            json.dump(self.pokemon_list, fichier,indent=4)

    
    def get_pokemon_list(self):
        try:
            with open('pokemon.json', 'r') as fichier:
                pokemon_list = json.load(fichier)
        except FileNotFoundError:
                pokemon_list = []
        return pokemon_list
#
#  Build the list updated
    def add_to_list(self,new_pokemon):
        if new_pokemon not in pokemon_list:
            self.pokemon_list.append(new_pokemon) 
        else:
            return print('Ce pokemon est déjà dans votre pokedex')

#name, lifePoint, level, XP, evolution, giveXP, limitXP,  attack, defence, type1, type2,
    
    def add_pokemon(self):
        name = input("Nom du Pokémon : ")
        pv = int(input("Points de vie : "))
        type = input("Type : ")
        attack = int(input("Attaque : "))
        defense = int(input("Défense : "))
        giveXP = int(input("Rapporte combien de points d'XP ? :"))

        new_pokemon = {"name": name, "lifePoint": pv, "level" : 1, "XP" : 0,"evolution" : False, 
                       "giveXP" : giveXP, "limitXP" :60, "attack": attack, "defense": defense, "type1": type, 
                       "type2": None}
        self.add_to_list(new_pokemon)
        print(f"{name} a été ajouté !") 
        


pikachu = { "name" : "Pikachu", "lifepoint": 10,"level": 1, 
                             "experience": 0, "attack": 1, "defense" : 1, "type": "Electrique"}
 

lugia =  { "name" : "Lugia", "lifepoint": 10,"level": 1, 
                             "experience": 0, "attack": 1, "defense" : 1, "type": "Air"}
 

salameche = {"name" : "Salameche", "lifepoint": 10,"level": 1, 
                             "experience": 0, "attack": 1, "defense" : 1, "type": "Feu"}

carapuce = {"name" : "Carapuce", "lifepoint": 10,"level": 1, 
                             "experience": 0, "attack": 1, "defense" : 1, "type": "Feu"}
roudoudou = {"name" : "Roudoudou", "lifepoint": 10,"level": 1, 
                             "experience": 0, "attack": 1, "defense" : 1, "type": "Feu"}





""" Building a Bank using the Pokemon_Bank class"""

# a new Pokemon_Bank instance
original_bank = Pokemon_bank("Pokemon Bank")

# Test le contenu de la liste
pokemon_list= original_bank.get_pokemon_list()
print(pokemon_list)

# records in a list with class method
original_bank.add_to_list(pikachu)
original_bank.add_to_list(lugia)
original_bank.add_to_list(salameche)
original_bank.add_to_list(carapuce)
original_bank.add_to_list(roudoudou)

# Add a new Pokemon, created by the player
original_bank.add_pokemon()

# Record the list in The Json File
original_bank.record_pokemon()


#Read file content
with open('pokemon.json', 'r') as fichier:
    pokemon_list = json.load(fichier)
print(pokemon_list)