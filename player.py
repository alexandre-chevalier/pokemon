import json
import os

class Player:
    def __init__(self, pokemon_filepath, players_filepath):
        self.name = input("Entrez votre nom: ")
        if self.player_exists(players_filepath):
            print(f"Vous avez déjà un compte avec ce nom.")
            self.pokemon = self.choose_pokemon(pokemon_filepath, players_filepath)
        else:
            self.pokemon = self.choose_pokemon(pokemon_filepath, players_filepath)

    def player_exists(self, filepath):
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r') as file:
                    players = json.load(file)
                    for player in players:
                        if player['name'] == self.name:
                            return True
            except json.JSONDecodeError:
                return False
        return False

    def choose_pokemon(self, pokemon_filepath, players_filepath):
        while True:
            try:
                with open(pokemon_filepath, 'r') as file:
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

    def save_to_file(self, filepath):
        player_data = {
            "name": self.name,
            "pokemon": self.pokemon
        }

        if os.path.exists(filepath):
            try:
                with open(filepath, 'r') as file:
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
                    self.pokemon = self.choose_pokemon('C:/Users/kylli/Desktop/Spe_ia/pokemon/pokemon.json', filepath)
                    player['pokemon'] = self.pokemon
                else:
                    return

        data.append(player_data)

        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)

if __name__ == "__main__":
    player = Player('C:/Users/kylli/Desktop/Spe_ia/pokemon/pokemon.json', 'C:/Users/kylli/Desktop/Spe_ia/pokemon/players.json')
    player.save_to_file('C:/Users/kylli/Desktop/Spe_ia/pokemon/players.json')