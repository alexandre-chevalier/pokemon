import json

# entries structures => "pokemon" : {"name" : "", "lifepoint": 10,"level": 1, "experience": 0, "attack": 1, "defense" : 1, "type": ""}
class Pokemon_bank:
    def __init__ (self, name):
        self.name = name
        self.pokemon_list = []

#Record entry in pokemon.json
    def record_pokemon(self):
        with open('pokemon.json', 'w') as fichier:
            json.dump(self.pokemon_list, fichier,indent=4)

    def get_pokemon_list(self):
        try:
            with open('pokemon.json', 'r') as fichier:
                pokemon_list = json.load(fichier)
        except FileNotFoundError:
                pokemon_list = []

    def record_new_pokemon(self,pokemon):
          self.pokemon_list.append(pokemon) 

pikachu = { "name" : "Pikachu", "lifepoint": 10,"level": 1, 
                             "experience": 0, "attack": 1, "defense" : 1, "type": "Electrique"}
 

lugia =  { "name" : "Lugia", "lifepoint": 10,"level": 1, 
                             "experience": 0, "attack": 1, "defense" : 1, "type": "Air"}
 

salameche = {"salameche" : { "name" : "Salameche", "lifepoint": 10,"level": 1, 
                             "experience": 0, "attack": 1, "defense" : 1, "type": "Feu"}}

original_bank = Pokemon_bank("Pokemon Bank")
original_bank.record_new_pokemon(pikachu)
original_bank.record_new_pokemon(lugia)

original_bank.record_pokemon()


#Read file content
with open('pokemon.json', 'r') as fichier:
    pokemon_list = json.load(fichier)
print(pokemon_list)