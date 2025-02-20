import json
import os
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
Pokemon_list = os.path.join(BASE_DIR, "data/pokemon.json")
class Player:
    def __init__(self, name):
        self.name = name
        self.pokemon_file = Pokemon_list
        self.player_file = "pokemon/players.json"
        self.pokemon = None

        """ if self.player_exists(self.player_file):
            print(f"Vous avez déjà un compte avec ce nom.")
            self.pokemon = self.choose_pokemon(self.pokemon_file, self.player_file)
        else:
            self.pokemon = self.choose_pokemon(self.pokemon_file, self.player_file)"""
       
    def player_exists(self):
        if os.path.exists(self.player_file):
            try:
                with open(self.player_file, 'r') as file:
                    players = json.load("player.json")
                    for player in players:
                        if player['name'] == self.name:
                            return True
            except json.JSONDecodeError:
                return False
        return False

    def choose_pokemon(self, choice):
        try:
            with open(self.pokemon_file, 'r') as file:
                pokemon_list = json.load( self.pokemon_file)
        except FileNotFoundError:
            print("Le fichier des Pokémon n'a pas été trouvé.")
            return None

        print("Choisissez un Pokémon parmi la liste suivante:")
        for index, pokemon in enumerate(pokemon_list, start=1):
            print(f"{index}. {pokemon['name']}")

        if choice.isdigit() and 1 <= int(choice) <= len(pokemon_list):
            chosen_pokemon = pokemon_list[int(choice) - 1]
            print(f"Vous avez choisi {chosen_pokemon['name']}.")
            self.pokemon = chosen_pokemon
            return chosen_pokemon
        else:
            print("Entrée invalide. Veuillez entrer un numéro valide.")
            return None

    def save_to_file(self, name):
        player_data = {
            "name": name,
            "pokemon": self.pokemon,
            "score": 0
        }

        if os.path.exists(self.player_file):
            try:
                with open(self.player_file, 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                data = []
        else:
            data = []

        # Vérifier si le joueur existe déjà
        for player in data:
            if player['name'] == self.name:
                print(f"Le joueur {self.name} existe déjà avec le Pokémon {player['pokemon']['name']}.")

        data.append(player_data)

        with open(self.player_file, 'w') as file:
            json.dump(data, file, indent=4)

    # Getter for name
    def get_name(self):
        return self.name

    # Setter for name
    def set_name(self, name):
        self.name = name

    # Getter for pokemon
    def get_pokemon(self):
        return self.pokemon

    # Setter for pokemon
    def set_pokemon(self, pokemon):
        self.pokemon = pokemon

    def battle(self):
        try:
            with open(self.pokemon_file, 'r') as file:
                pokemon_list = json.load(self.pokemon_file)
        except FileNotFoundError:
            print("Le fichier des Pokémon n'a pas été trouvé.")
            return None

        if not self.pokemon:
            print("Vous n'avez pas de Pokémon pour combattre.")
            return None

        opponent_pokemon = random.choice(pokemon_list)
        print(f"Votre Pokémon {self.pokemon['name']} affronte {opponent_pokemon['name']}.")

        # Simulate battle (simple random win/lose for demonstration)
        if random.choice([True, False]):
            print(f"Félicitations! {self.pokemon['name']} a gagné contre {opponent_pokemon['name']}.")
            self.pokemon = opponent_pokemon  # Player wins and gets the opponent's Pokémon
        else:
            print(f"Dommage! {self.pokemon['name']} a perdu contre {opponent_pokemon['name']}.")
            self.pokemon = None  # Player loses their Pokémon

        self.save_to_file(self.name)

