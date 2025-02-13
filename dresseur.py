import pygame
import json
from manage_pokemon_list import *
# dresseur.py

class Dresseur:
    
    def __init__(self, player_name):
        """Initialise un dresseur avec un nom et une équipe de Pokémon vide"""
        self.player_name = player_name
        self.pokemonTeam = []

    def add_pokemon(self, pokemon):
        """Ajoute un Pokémon à l'équipe du dresseur (max 6)."""
        if len(self.pokemonTeam) < 6:
            self.pokemonTeam.append(pokemon)
            print(f"{pokemon['name']} a été ajouté à l'équipe de {self.player_name}!")
        else:
            print(f"{self.player_name} ne peut pas avoir plus de 6 Pokémon dans son équipe!")

    def choose_pokemons(self, pokemon_list):
        """Permet à l'utilisateur de choisir 6 Pokémon parmi la liste"""
        print(f"{self.player_name}, choisissez vos 6 Pokémon !")
        for i in range(6):
            print(f"Pokémon {i+1}:")
            for idx, pokemon in enumerate(pokemon_list):
                print(f"{idx + 1}. {pokemon['name']}")
            
            choice = int(input(f"Choisissez le Pokémon {i+1} (par numéro) : "))
            if 1 <= choice <= len(pokemon_list):
                self.add_pokemon(pokemon_list[choice - 1])
            else:
                print("Choix invalide, essayez encore.")
    
    def display_pokemonTeam(self):
        """Affiche les Pokémon de l'équipe du dresseur."""
        print(f"L'équipe de {self.player_name} est :")
        if not self.pokemonTeam:
            print("Aucun Pokémon dans l'équipe.")
        for index, pokemon in enumerate(self.pokemonTeam):
            print(f"{index + 1}. {pokemon['name']}")

