import os
import json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "data/images")
SOUND_DIR = os.path.join(BASE_DIR, "data/sounds")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
Pokemon_list = os.path.join(BASE_DIR, "data/pokemon.json")
player_list = os.path.join(BASE_DIR, "data/players.json")
POKEDEX_FILE = os.path.join(BASE_DIR, "data/poke.json")

with open(POKEDEX_FILE, 'r', encoding='utf-8') as fichier:
    contenu = fichier.read().strip()
    if not contenu:
            raise ValueError("Le fichier est vide")
            pokedex_list = json.loads(contenu)
print(contenu)