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
        return pokemon_list
# Build the list updated
    def record_new_pokemon(self,pokemon):
          self.pokemon_list.append(pokemon) 

pikachu = { "name" : "Pikachu", "lifepoint": 10,"level": 1, 
                             "experience": 0, "attack": 1, "defense" : 1, "type": "Electrique"}
 

lugia =  { "name" : "Lugia", "lifepoint": 10,"level": 1, 
                             "experience": 0, "attack": 1, "defense" : 1, "type": "Air"}
 

salameche = {"name" : "Salameche", "lifepoint": 10,"level": 1, 
                             "experience": 0, "attack": 1, "defense" : 1, "type": "Feu"}

carapuce = {"name" : "Carapuce", "lifepoint": 10,"level": 1, 
                             "experience": 0, "attack": 1, "defense" : 1, "type": "Feu"}
roudoudou = {"name" : "Roudoudou", "lifepoint": 10,"level": 1, 
                             "experience": 0, "attack": 1, "defense" : 1, "type": "Feu"}





""" Building a Bank using the Pokemon_Bank class"""

# a new Pokemon_Bank instance
original_bank = Pokemon_bank("Pokemon Bank")

# Test le contenu de la liste
pokemon_list= original_bank.get_pokemon_list()
print(pokemon_list)

# records in a list with class method
original_bank.record_new_pokemon(pikachu)
original_bank.record_new_pokemon(lugia)
original_bank.record_new_pokemon(salameche)
original_bank.record_new_pokemon(carapuce)
original_bank.record_new_pokemon(roudoudou)

# Record the list in The Json File
original_bank.record_pokemon()


#Read file content
with open('pokemon.json', 'r') as fichier:
    pokemon_list = json.load(fichier)
print(pokemon_list)