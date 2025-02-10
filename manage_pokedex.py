import random
import json

""" Manage POKEDEX Json file """

class Pokedex:
    def __init__(self, name):
        self.name = name
        self.pokemon_list = []
    
    def choose_pokemon_random(self):
        with open('pokemon.json', 'r') as file:
            self.pokemon_list = json.load(file)
       
        pokemon_sample = random.sample(self.pokemon_list, 1) # Randomly chooses 1 element from pokemon_list
        return pokemon_sample

    def deck_building(self):
        new_deck = self.choose_pokemon_random() # Calls the sample function
        return new_deck




# Pokedex instance
player_1 = Pokedex("player_deck")

# deck created by calling the deck_building function
print(player_1.deck_building())
