import json

import os

filename = "pokemon_list.json"

if not os.path.exists(filename):
    print(f"Erreur : {filename} n'existe pas dans {os.getcwd()}")
