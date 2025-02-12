import json

class history : 
    def __init__ (self, players_file):
        self.players_file = players_file

    def record_history(score, player_name):
            
            try:
                with open("players.json", "r") as f:
                    players_container = json.load(f)
            except FileNotFoundError:
                # if the file doesn't exist=> a new list
                players_container = []
            except json.JSONDecodeError:
                # if the file is not good => a new list
                players_container = []
            
            # update player or add a new player
            player_found = False
            for player in players_container:
                if player["name"] == player_name:
                    player["score"] += score
                    player["pokedex"] = player_name
                    player_found = True
                    break
            
            if not player_found:
                players_container.append({"name": player_name, "score": score, "pokedex" : player_name})
            
            # Trier les scores par ordre décroissant
            players_container = sorted(players_container, key=lambda x: x["score"], reverse=True)
            
            # Enregistrer les scores dans le fichier
            with open("players.json", "w") as f:
                json.dump(players_container, f, indent=4)  # indent=4 pour un formatage lisible

    def get_player_history():
        with open ("players.json", "r") as file:
            players_container = json.load(file)      
