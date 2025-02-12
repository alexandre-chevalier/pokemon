import json
from alex import * 
import os

BASE_DIR = r"C:\Users\Windows\Desktop\projets\1a\pokemon"
IMAGE_DIR = os.path.join(BASE_DIR, "images")

# entries structures => "pokemon" : {"name" : "", "lifepoint": 10,"level": 1, "experience": 0, "attack": 1, "defense" : 1, "type": ""}
class Pokemon_bank:
    def __init__ (self, name):
        self.name = name
        self.pokemon_list =[]

#Record entry in pokemon.json
    def record_pokemon(self):
        with open('pokemon_list.json', 'w') as fichier:
            json.dump(self.pokemon_list, fichier,indent=4)

    
    def get_pokemon_list(self):
        try:
            with open('pokemon_list.json', 'r') as fichier:
                pokemon_list = json.load(fichier)
        except FileNotFoundError:
                pokemon_list = []
        return pokemon_list

#  Build the list updated
    def add_to_list(self, new_pokemon):

        new_pokemon_dict = new_pokemon.to_dict()

        # Vérifie si le Pokémon existe déjà dans la liste
        if new_pokemon_dict not in self.pokemon_list:
            self.pokemon_list.append(new_pokemon_dict)
            self.record_pokemon()  # Enregistre la liste mise à jour
        else:
            print('Ce pokemon est déjà dans votre pokedex')

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
        

# a new Pokemon_Bank instance
pokemon = Pokemon_bank("original_bank")

pikachu = Pikachu()
carapuce =Carapuce()
salameche =Salameche()
bulbizarre = Bulbizarre()
lugia = Lugia()
artikodin = Artikodin()
triopiqueur =Triopiqueur()


pokemon.add_to_list(pikachu)
pokemon.add_to_list(carapuce)
pokemon.add_to_list(salameche)
pokemon.add_to_list(bulbizarre)
pokemon.add_to_list(artikodin)
pokemon.add_to_list(triopiqueur)
list_poke = pokemon.get_pokemon_list()
print(list_poke)