import json

class BattleManager:
    def __init__(self, player_file="players.json"):
        self.player_file = player_file
        self.players = self.load_players()

    def load_players(self):
        try:
            with open(self.player_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_players(self):
        with open(self.player_file, "w") as file:
            json.dump(self.players, file, indent=4)

    def find_player(self, player_name):
        for player in self.players:
            if player["name"] == player_name:
                return player
        return None

    def record_winner(self, winner, loser):
        player = self.find_player(winner.name)
        if player:
            # Ajouter le Pokémon vaincu à l'équipe du joueur
            player["pokemon"] = loser.__dict__
            print(f"{winner.name} a gagné {loser.name}!")
            self.save_players()
        
    def remove_loser_pokemon(self, loser):
        for player in self.players:
            if player["pokemon"]["name"] == loser.name:
                player.pop("pokemon", None)  # Supprime le Pokémon du joueur
                print(f"{loser.name} a été retiré de l'équipe.")
                self.save_players()
                break