import random
import json

""" Manage POKEDEX Json file """

""" Constitution of the starting deck """

def choose_pokemon_random():
    with open('pokemon.json', 'r') as file:
        pokemon_list = json.load(file)
       
    pokemon_sample = random.sample(pokemon_list, 1) # Randomly chooses 1 element from pokemon_list
    return pokemon_sample

def deck_building():
    new_deck = choose_pokemon_random() # Calls the sample function
    return new_deck

# deck created by calling the deck_building function
print(deck_building())
