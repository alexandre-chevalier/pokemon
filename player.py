import json
import os

class Player:
    def __init__(self, name):
        self.name = name
        self.pokemon_file = "pokemon\pokemon.json"
        self.player_file = "pokemon\players.json"
        """if self.player_exists(players_filepath):
            print(f"Vous avez déjà un compte avec ce nom.")
            self.pokemon = self.choose_pokemon(pokemon_filepath, players_filepath)
        else:
            self.pokemon = self.choose_pokemon(pokemon_filepath, players_filepath)
"""
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

    def choose_pokemon(self):
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

            choice = input("Entrez le numéro du Pokémon choisi: ")
            if choice.isdigit() and 1 <= int(choice) <= len(pokemon_list):
                chosen_pokemon = pokemon_list[int(choice) - 1]
                print(f"Vous avez choisi {chosen_pokemon['name']}. Voulez-vous confirmer ce choix ? (oui/non)")
                confirm = input().lower()
                if confirm == 'oui':
                    return chosen_pokemon
            else:
                print("Entrée invalide. Veuillez entrer un numéro valide.")

    def save_to_file(self):
        player_data = {
            "name": self.name,
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
                print("Voulez-vous choisir un nouveau Pokémon ? (oui/non)")
                confirm = input().lower()
                if confirm == 'oui':
                    self.pokemon = self.choose_pokemon('C:/Users/kylli/Desktop/Spe_ia/pokemon/pokemon.json', self.player_file)
                    player['pokemon'] = self.pokemon
                else:
                    return

        data.append(player_data)

        with open(self.player_file, 'w') as file:
            json.dump(data, file, indent=4)

if __name__ == "__main__":
    player = Player('C:/Users/kylli/Desktop/Spe_ia/pokemon/pokemon.json', 'C:/Users/kylli/Desktop/Spe_ia/pokemon/players.json')
    player.save_to_file('C:/Users/kylli/Desktop/Spe_ia/pokemon/players.json')