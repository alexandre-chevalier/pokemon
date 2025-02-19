import json

class Pokedex:
    
    def __init__(self, name):
        
        self.name = name
        self.pokedex_list = []
        self.pokemon_met = [{'name': 'pikachu', 'lifePoint': 100, 'level': 1, 'experience': 0, 'giveXp': 10, 'limitXP': 20, 'attack': 10, 'defence': 8, 'type1': 'electric', 'type2': None, 'KO': False, 'link_image': 'images', 'statut': 'normal', 'next_evolution': {'name': 'raichu', 'lifePoint': 250, 'level': 1, 'experience': 0, 'giveXp': 100, 'limitXP': 120, 'attack': 30, 'defence': 25, 'type1': 'electric', 'type2': None, 'KO': False, 'link_image': 'images', 'statut': 'normal', 'next_evolution': None}}, 
                            
                            ]


     # Get pokedex from podex.json   
    def get_pokedex_list(self): # Get pokedex and create a pokedex if none
        try:
            with open('poke.json', 'r') as fichier:
                self.pokedex_list = json.load(fichier)
        except FileNotFoundError:
                self.pokedex_list = []
        return self.pokedex_list    
    

    
    def record_pokedex(self):
            self.get_pokedex_list()
            self.entry = {self.name : self.pokemon_met}
            self.pokedex_list.append(self.entry)
            with open('poke.json', 'w') as fichier:
                json.dump(self.pokedex_list, fichier,indent=4)
    


player_name = input(" Joueur")
pokedex= Pokedex(player_name)
pokedex.record_pokedex()
pokedex_list = pokedex.get_pokedex_list()
print(pokedex_list)