import random
import json
from pokemon import *
class Combat:
    def __init__(self, player_pokemon, opponent_pokemon):
        self.player_pokemon = player_pokemon
        self.opponent_pokemon = opponent_pokemon
        self.pokedex_file = 'pokedex.json'
        self.pokedex={}
        self.load_pokedex()

    def load_pokedex(self):
        """Charge le Pokédex depuis le fichier JSON."""
        if os.path.exists(self.pokedex_file):
            with open(self.pokedex_file, 'r') as file:
                self.pokedex = json.load(file)
        else:
            self.pokedex = {}

    def save_pokedex(self):
        """Sauvegarde le Pokédex dans le fichier JSON."""
        with open(self.pokedex_file, 'w') as file:
            json.dump(self.pokedex, file, indent=4)

    def calculate_damage(self, attacker, defender):
        """Calcule les dégâts infligés par l'attaquant au défenseur."""
        type_effectiveness = {
            ("Eau", "Feu"): 2, ("Feu", "Plante"): 2, ("Plante", "Eau"): 2, ("Électrik", "Eau"): 2,
            ("Eau", "Terre"): 0.5, ("Feu", "Eau"): 0.5, ("Plante", "Feu"): 0.5, ("Électrik", "Terre"): 0,
            ("Feu", "Feu"): 1, ("Eau", "Eau"): 1, ("Plante", "Plante"): 1, ("Terre", "Terre"): 1,
            ("Normal", "Normal"): 1, ("Normal", "Feu"): 1, ("Normal", "Eau"): 1, ("Normal", "Plante"): 1,
        }
        effectiveness = type_effectiveness.get((attacker.type1, defender.type1), 1)
        effectiveness *= type_effectiveness.get((attacker.type1, defender.type2), 1)
        effectiveness *= type_effectiveness.get((attacker.type2, defender.type1), 1)
        effectiveness *= type_effectiveness.get((attacker.type2, defender.type2), 1)

        # Calcul des dégâts
        base_damage = attacker.attack - defender.defence
        if base_damage < 0:
            base_damage = 0
        damage = base_damage * effectiveness
        return max(damage, 0)

    def attack(self, attacker, defender):
        """Effectue une attaque de l'attaquant sur le défenseur."""
        damage = self.calculate_damage(attacker, defender)
        defender.lifePoint -= damage
        if defender.lifePoint <= 0:
            defender.lifePoint = 0
            defender.is_ko()
        return damage

    def battle(self):
        """Gère le déroulement du combat entre les deux Pokémon."""
        print(f"Début du combat entre {self.player_pokemon.name} et {self.opponent_pokemon.name}!")

        while not self.player_pokemon.KO and not self.opponent_pokemon.KO:
            # Tour du joueur
            damage = self.attack(self.player_pokemon, self.opponent_pokemon)
            print(f"{self.player_pokemon.name} attaque {self.opponent_pokemon.name} et inflige {damage} points de dégâts.")
            if self.opponent_pokemon.KO:
                print(f"{self.opponent_pokemon.name} est KO!")
                break

            # Tour de l'adversaire
            damage = self.attack(self.opponent_pokemon, self.player_pokemon)
            print(f"{self.opponent_pokemon.name} attaque {self.player_pokemon.name} et inflige {damage} points de dégâts.")
            if self.player_pokemon.KO:
                print(f"{self.player_pokemon.name} est KO!")
                break

        # Enregistrement des Pokémon dans le Pokédex
        #self.record_pokemon(self.player_pokemon)
        #self.record_pokemon(self.opponent_pokemon)
        self.save_pokedex()

    #def record_pokemon(self, pokemon):
       # """Enregistre un Pokémon dans le Pokédex si ce n'est pas déjà fait."""
       # if pokemon.name not in self.pokedex:
          #  self.pokedex[pokemon.name] = pokemon.to_dict()

    def menu(self):
        while True:
            print("1. Lancer une partie")
            print("2. Accéder au Pokédex")
            choix = input("Choix : ")

            if choix == "1":
                self.battle()  
            elif choix == "2":
                print(self.pokedex)
            else:
                print("Choix invalide.")

# Lancer le menu principal
jeu = Combat(pikachu, tortank)
jeu.menu()                
