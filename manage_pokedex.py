import random
import json

""" Manage POKEDEX Json file """

class Pokedex:
    
    def __init__(self, name):
        
        self.name = name
        self.pokemon_list = []
        self.pokedex_list = []
    
    def choose_pokemon_random(self):
        with open('pokemon.json', 'r') as file:#load all pokemons from pokemon.json
            self.pokemon_list = json.load(file)
       
        pokemon_sample = random.sample(self.pokemon_list, 4) # Randomly chooses 1 element from pokemon_list
        return pokemon_sample

    def deck_building(self):
        new_deck = self.choose_pokemon_random() # Calls the sample function
        return new_deck
    
    def record_pokedex(self):
        with open('pokedex.json', 'w') as fichier:
            json.dump(self.pokedex_list, fichier,indent=4)

    
    def get_pokedex_list(self): # Get pokedex and create a pokedex if none
        try:
            with open('pokedex.json', 'r') as fichier:
                self.pokedex_list = json.load(fichier)
        except FileNotFoundError:
                self.pokedex_list = []
        return self.pokedex_list
    
    





# Pokedex instance
player_1 = Pokedex("player_deck")

# deck created by calling the deck_building function
player_1.deck_building()
player_1.deck_building()


player_1.pokedex_list = player_1.deck_building()
player_1.record_pokedex()

#print(player_1.record_pokedex())
print(player_1.get_pokedex_list())


