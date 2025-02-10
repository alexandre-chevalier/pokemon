import json

# entries structures => "pokemon" : {"name" : "", "lifepoint": 10,"level": 1, "experience": 0, "attack": 1, "defense" : 1, "type": ""}

pokemon_list = []

#Record entry in pokemon.json
def record_pokemon():
    with open('pokemon.json', 'w') as fichier:
        json.dump(pokemon_list, fichier,indent=4)

def get_pokemon_list():
    try:
        with open('pokemon.json', 'r') as fichier:
            pokemon_list = json.load(fichier)
    except FileNotFoundError:
        pokemon_list = []

pikachu = { "name" : "Pikachu", "lifepoint": 10,"level": 1, 
                             "experience": 0, "attack": 1, "defense" : 1, "type": "Electrique"}
 

lugia =  { "name" : "Lugia", "lifepoint": 10,"level": 1, 
                             "experience": 0, "attack": 1, "defense" : 1, "type": "Air"}
 

salameche = {"salameche" : { "name" : "Salameche", "lifepoint": 10,"level": 1, 
                             "experience": 0, "attack": 1, "defense" : 1, "type": "Feu"}}

pokemon_list.append(lugia) 
pokemon_list.append(salameche)  
pokemon_list.append(pikachu)

record_pokemon()

#Read file content
with open('pokemon.json', 'r') as fichier:
    pokemon_list = json.load(fichier)
print(pokemon_list)