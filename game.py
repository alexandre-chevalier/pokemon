import random
import json
import os

class Pokemon:
    def __init__(self, name, lifePoint, level, XP, giveXP, limitXP, attack, defence, type1, type2=None, next_evolution=None):
        self.name = name
        self.lifePoint = lifePoint
        self.level = level
        self.experience = XP
        self.giveXp = giveXP
        self.limitXP = limitXP
        self.attack = attack
        self.defence = defence
        self.type1 = type1
        self.type2 = type2
        self.next_evolution = next_evolution
        self.status_effects = {}
        self.KO = False

    def decrement_status_effects(self):
        for effect in list(self.status_effects.keys()):
            if self.status_effects[effect] > 0:
                self.status_effects[effect] -= 1
            if self.status_effects[effect] == 0:
                del self.status_effects[effect]

class SpecialMove:
    def __init__(self, name, damage, accuracy, effects=None):
        self.name = name
        self.damage = damage
        self.accuracy = accuracy
        self.effects = effects

    def apply_effect(self, target):
        if self.effects and random.random() < self.effects["chance"]:
            effect = self.effects["status"]
            target.status_effects[effect] = self.effects["duration"]
            print(f"{target.name} is affected by {effect}!")

class Game:
    def __init__(self, combat):
        self.combat = combat

    def run(self):
        self.combat.start_battle()

class Combat:
    TYPE_EFFICACY = {
        ("Spectre", "Spectre"): 2, ("Spectre", "Psy"): 2, ("Spectre", "Normal"): 0, ("Spectre", "Combat"): 0,
        ("Acier", "Glace"): 2, ("Acier", "Roche"): 2, ("Acier", "Acier"): 0.5, ("Acier", "Feu"): 0.5, ("Acier", "Eau"): 0.5, ("Acier", "Électrik"): 0.5,
        ("Psy", "Combat"): 2, ("Psy", "Poison"): 2, ("Psy", "Acier"): 0.5, ("Psy", "Ténèbres"): 0,
        ("Combat", "Normal"): 2, ("Combat", "Roche"): 2, ("Combat", "Glace"): 2, ("Combat", "Acier"): 2, ("Combat", "Spectre"): 0, ("Combat", "Poison"): 0.5, ("Combat", "Vol"): 0.5, ("Combat", "Psy"): 0.5, ("Combat", "Fée"): 0.5,
        ("Poison", "Plante"): 2, ("Poison", "Fée"): 2, ("Poison", "Poison"): 0.5, ("Poison", "Sol"): 0.5, ("Poison", "Roche"): 0.5, ("Poison", "Spectre"): 0.5, ("Poison", "Acier"): 0,
        ("Ténèbres", "Psy"): 2, ("Ténèbres", "Spectre"): 2, ("Ténèbres", "Combat"): 0.5, ("Ténèbres", "Fée"): 0.5,
        ("Fée", "Combat"): 2, ("Fée", "Dragon"): 2, ("Fée", "Ténèbres"): 2, ("Fée", "Feu"): 0.5, ("Fée", "Poison"): 0.5, ("Fée", "Acier"): 0.5,
        ("Dragon", "Dragon"): 2, ("Dragon", "Fée"): 0,
        ("Électrik", "Eau"): 2, ("Électrik", "Vol"): 2, ("Électrik", "Électrik"): 0.5, ("Électrik", "Plante"): 0.5, ("Électrik", "Dragon"): 0.5, ("Électrik", "Sol"): 0
    }

    def __init__(self, player):
        self.player = player
        pokemon_list = self.load_pokemon_list()
        self.pokemon2 = random.choice(pokemon_list)
        self.pokemon1 = self.load_player_pokemon()
        self.special_moves = [
            SpecialMove("Fire Blast", 50, 0.85, {"status": "burn", "chance": 0.3, "duration": 5}),
            SpecialMove("Thunderbolt", 45, 0.9, {"status": "paralysis", "chance": 0.2, "duration": 4}),
            SpecialMove("Ice Beam", 40, 0.95, {"status": "freeze", "chance": 0.1, "duration": 3}),
        ]
        self.game = Game(self)

    def apply_status_effects(self, pokemon):
        pokemon.decrement_status_effects()
        for effect, duration in pokemon.status_effects.items():
            if effect == "burn":
                pokemon.lifePoint -= 5
                print(f"{pokemon.name} is hurt by burn!")
            elif effect == "paralysis" and random.random() < 0.5:
                print(f"{pokemon.name} is paralyzed and can't move!")
                return True
            elif effect == "freeze" and random.random() < 0.2:
                print(f"{pokemon.name} is frozen solid!")
                return True
        return False

    def display_status_effects(self, pokemon):
        if pokemon.status_effects:
            effects_text = ", ".join(pokemon.status_effects.keys())
            print(f"Status: {effects_text}")

    def load_player_pokemon(self):
        pokemon_data = self.player.pokemon
        expected_keys = {"name", "lifePoint", "level", "XP", "giveXP", "limitXP", "attack", "defence", "type1", "type2", "next_evolution"}
        filtered_data = {k: v for k, v in pokemon_data.items() if k in expected_keys}
        return Pokemon(**filtered_data)

    def load_pokemon_list(self):
        try:
            with open('pokemon.json', 'r') as file:
                data = json.load(file)
                expected_keys = {"name", "lifePoint", "level", "XP", "giveXP", "limitXP", "attack", "defence", "type1", "type2", "next_evolution"}
                return [Pokemon(**{k: v for k, v in p.items() if k in expected_keys}) for p in data]
        except FileNotFoundError:
            print("Error: 'pokemon.json' file not found.")
            return []
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in 'pokemon.json'.")
            return []

    def calculate_multiplier(self, attacker, target):
        multiplier1 = self.TYPE_EFFICACY.get((attacker.type1, target.type1), 1)
        multiplier2 = self.TYPE_EFFICACY.get((attacker.type1, target.type2), 1) if target.type2 else 1
        multiplier3 = self.TYPE_EFFICACY.get((attacker.type2, target.type1), 1) if attacker.type2 else 1
        multiplier4 = self.TYPE_EFFICACY.get((attacker.type2, target.type2), 1) if attacker.type2 and target.type2 else 1
        return multiplier1 * multiplier2 * multiplier3 * multiplier4

    def attack(self, attacker, target, move=None):
        if not move:
            move = random.choice(self.special_moves)
        if random.random() < move.accuracy:
            multiplier = self.calculate_multiplier(attacker, target)
            damage = max(0, (attacker.attack * multiplier * move.damage / 100) - target.defence)
            target.lifePoint -= damage
            print(f"{attacker.name} uses {move.name} on {target.name} with a multiplier of {multiplier}. Damage dealt: {damage}")
            move.apply_effect(target)
            if target.lifePoint <= 0:
                target.KO = True
                print(f"{target.name} is K.O. !")
        else:
            print(f"{attacker.name}'s attack missed!")

    def get_pokedex_list(self):
        try:
            with open('poke.json', 'r', encoding='utf-8') as file:
                contenu = file.read().strip()
                if not contenu:
                    raise ValueError("Le fichier est vide")
                self.pokedex_list = json.loads(contenu)
        except (FileNotFoundError, ValueError, json.JSONDecodeError):
            print("Le fichier poke.json est vide ou invalide. Réinitialisation...")
            self.pokedex_list = []
            with open('poke.json', 'w', encoding='utf-8') as file:
                json.dump(self.pokedex_list, file, indent=4)
        return self.pokedex_list

    def record_pokedex(self, pokemon):
        self.get_pokedex_list()
        if not self.player:
            return
        player_name = self.player.name
        player_found = False
        for entry in self.pokedex_list:
            if player_name in entry:
                pokemon_dict = entry[player_name]
                if pokemon.name in pokemon_dict:
                    pokemon_dict[pokemon.name]["count"] += 1
                else:
                    pokemon_dict[pokemon.name] = {
                        "count": 1,
                        "lifePoint": pokemon.lifePoint,
                        "level": pokemon.level,
                        "attack": pokemon.attack,
                        "defence": pokemon.defence,
                        "type1": pokemon.type1,
                        "type2": pokemon.type2,
                    }
                entry[player_name] = pokemon_dict
                player_found = True
                break
        if not player_found:
            self.pokedex_list.append({
                player_name: {
                    pokemon.name: {
                        "count": 1,
                        "lifePoint": pokemon.lifePoint,
                        "level": pokemon.level,
                        "attack": pokemon.attack,
                        "defence": pokemon.defence,
                        "type1": pokemon.type1,
                        "type2": pokemon.type2,
                    }
                }
            })
        try:
            with open('poke.json', 'w', encoding='utf-8') as file:
                json.dump(self.pokedex_list, file, indent=4, ensure_ascii=False)
            print("Données enregistrées dans poke.json")
        except Exception as e:
            print(f"Erreur lors de l'enregistrement dans poke.json: {e}")

    def record_winner(self, winner, looser):
        winner.experience += looser.giveXp
        print(f"{winner.name} gagne {looser.giveXp} XP ! XP total: {winner.experience}/{winner.limitXP}")
        if winner.experience >= winner.limitXP:
            winner.level += 1
            winner.experience -= winner.limitXP
            winner.limitXP *= 3
            winner.attack += 2
            winner.defence += 2
            print(f"{winner.name} monte au niveau {winner.level} !")
        try:
            with open("players.json", "r") as f:
                players_data = json.load(f)
            for player in players_data:
                if player["pokemon"]["name"] == winner.name:
                    player["pokemon"]["XP"] = winner.experience
                    player["pokemon"]["level"] = winner.level
                    player["pokemon"]["limitXP"] = winner.limitXP
                    player["pokemon"]["attack"] = winner.attack
                    player["pokemon"]["defence"] = winner.defence
                    break
            with open("players.json", "w") as f:
                json.dump(players_data, f, indent=4)
                print(f"{winner.name} a été mis à jour dans players.json")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde de {winner.name} : {e}")
        with open("vainqueurs.json", "a") as f:
            json.dump({"vainqueur": winner.name}, f)
            f.write("\n")

    def draw_health_bar(self, current_hp, max_hp):
        bar_width = 100
        fill = (current_hp / max_hp) * bar_width
        bar = "#" * int(fill) + "-" * (bar_width - int(fill))
        print(f"[{bar}] {current_hp}/{max_hp}")

    def display_message(self, message):
        print(message)

    def display_end_message(self, winner, looser):
        self.display_message(f"{looser.name} is K.O. !")
        self.display_message(f"{winner.name} gains {looser.giveXp} XP! Total XP: {winner.experience}/{winner.limitXP}")
        self.display_message(f"{winner.name} has been updated in players.json")
        self.display_message(f"The winner is {winner.name}!")

    def display_turn(self, attacker_name):
        self.display_message(f"{attacker_name}'s turn to attack!")

    def display_winner(self, winner):
        self.display_message(f"Winner: {winner.name}!")

    def start_battle(self):
        self.display_message("Battle starts!")

        # Boucle principale du combat
        while not self.pokemon1.KO and not self.pokemon2.KO:
            # Tour du Pokémon 1
            self.display_turn(self.pokemon1.name)
            self.attack(self.pokemon1, self.pokemon2)
            if self.pokemon2.KO:
                break

            # Tour du Pokémon 2
            self.display_turn(self.pokemon2.name)
            self.attack(self.pokemon2, self.pokemon1)

        # Déterminer le gagnant et afficher le message de fin
        winner = self.pokemon1 if self.pokemon2.KO else self.pokemon2
        looser = self.pokemon2 if self.pokemon2.KO else self.pokemon1
        self.display_end_message(winner, looser)

        # Enregistrer le gagnant
        self.record_winner(winner, looser)

# Exemple d'utilisation
class Player:
    def __init__(self, name, pokemon):
        self.name = name
        self.pokemon = pokemon

# Initialisation d'un joueur et de son Pokémon
player_pokemon_data = {
    "name": "Pikachu",
    "lifePoint": 100,
    "level": 5,
    "XP": 0,
    "giveXP": 50,
    "limitXP": 100,
    "attack": 55,
    "defence": 40,
    "type1": "Électrik",
    "type2": None,
    "next_evolution": "Raichu"
}
player = Player("Ash", player_pokemon_data)

# Démarrer le combat
combat = Combat(player)
combat.start_battle()
