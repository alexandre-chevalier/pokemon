import json
import os

class Player:
    def __init__(self, name):
        self.name = name
        self.pokemon_file = "pokemon\pokemon.json"
        self.player_file = "pokemon\players.json"
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
                    players = json.load(file)
                    for player in players:
                        if player['name'] == self.name:
                            return True
            except json.JSONDecodeError:
                return False
        return False

    def choose_pokemon(self, choice):
        while True:
            try:
                with open(self.pokemon_file, 'r') as file:
                    pokemon_list = json.load(file)
            except FileNotFoundError:
                print("Le fichier des Pokémon n'a pas été trouvé.")
                return None

            print("Choisissez un Pokémon parmi la liste suivante:")
            for index, pokemon in enumerate(pokemon_list, start=1):
                print(f"{index}. {pokemon['name']}")

            if choice.isdigit() and 1 <= int(choice) <= len(pokemon_list):
                print(self.name)
                chosen_pokemon = pokemon_list[int(choice) - 1]
                print(f"Vous avez choisi {chosen_pokemon['name']}.")
                self.pokemon = chosen_pokemon
                print(self.pokemon)
                return chosen_pokemon
            else:
                print("Entrée invalide. Veuillez entrer un numéro valide.")

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

