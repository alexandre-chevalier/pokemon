import random
import json
import os
import pygame
from pokemon import Pokemon
from game import Game
from special_move import SpecialMove

# Screen size
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 223, 0)

BASE_DIR = r"C:\Users\ndiay\Desktop\new_pokemon"
IMAGE_DIR = os.path.join(BASE_DIR, "images")
SOUND_DIR = os.path.join(BASE_DIR, "sounds")
background_image = pygame.image.load(os.path.join(IMAGE_DIR, 'arene_ring.png'))

font_path = r"C:\Users\ndiay\Desktop\new_pokemon\assets\Audiowide-Regular.ttf"
font = pygame.font.Font(font_path, 36)

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
        self.pokemon1_image = self.load_and_scale_image(self.pokemon1.name, (150, 150))
        self.pokemon2_image = self.load_and_scale_image(self.pokemon2.name, (150, 150))
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

    def display_status_effects(self, pokemon, x, y):
        if pokemon.status_effects:
            effects_text = ", ".join(pokemon.status_effects.keys())
            status_text = font.render(f"Status: {effects_text}", True, YELLOW)
            self.game.screen.blit(status_text, (x, y))

    def load_player_pokemon(self):
        # Return the player's Pokémon as a Pokemon object
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

    def load_and_scale_image(self, pokemon_name, size):
        try:
            image_path = os.path.join(IMAGE_DIR, f"{pokemon_name}.png")
            image = pygame.image.load(image_path)
            return pygame.transform.scale(image, size)
        except pygame.error as e:
            print(f"Error loading image: {e}")
            return None

    def calculate_multiplier(self, attacker, target):
        multiplier1 = self.TYPE_EFFICACY.get((attacker.type1, target.type1), 1)
        multiplier2 = self.TYPE_EFFICACY.get((attacker.type1, target.type2), 1) if target.type2 else 1
        multiplier3 = self.TYPE_EFFICACY.get((attacker.type2, target.type1), 1) if attacker.type2 else 1
        multiplier4 = self.TYPE_EFFICACY.get((attacker.type2, target.type2), 1) if attacker.type2 and target.type2 else 1
        return multiplier1 * multiplier2 * multiplier3 * multiplier4

    def play_attack_sound(self):
        try:
            sound_path = os.path.join(SOUND_DIR, "attack2.mp3")
            pygame.mixer.Sound(sound_path).play()
        except pygame.error as e:
            print(f"Error loading sound: {e}")

    def attack(self, attacker, target, move=None):
        self.play_attack_sound()
        if not move:
            move = random.choice(self.special_moves)
        if random.random() < move.accuracy:
            multiplier = self.calculate_multiplier(attacker, target)
            damage = max(0, (attacker.attack * multiplier * move.damage / 100) - target.defence)
            target.lifePoint -= damage
            print(f"{attacker.name} uses {move.name} on {target.name} with a multiplier of {multiplier}. Damage dealt: {damage}")
            move.apply_effect(target)
            damage_text = font.render(f"{attacker.name} deals {damage} damage to {target.name}!", True, RED)
            self.game.screen.blit(damage_text, (50, 300))
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
            winner.XP -= winner.limitXP
            winner.limitXP *= 3
            winner.attack += 2
            winner.defence += 2
            message3 = font.render(f"{winner.name} monte au niveau {winner.level} !", True, YELLOW)
            self.game.screen.blit(message3, (50, 300))
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

    def draw_health_bar(self, surface, x, y, current_hp, max_hp):
        bar_width = 100
        bar_height = 10
        fill = (current_hp / max_hp) * bar_width
        pygame.draw.rect(surface, (255, 0, 0), (x, y, bar_width, bar_height))
        pygame.draw.rect(surface, (0, 255, 0), (x, y, fill, bar_height))

    def display_message(self, message, x, y, color=WHITE):
        message_surface = font.render(message, True, color)
        message_rect = message_surface.get_rect(topleft=(x, y))
        pygame.draw.rect(self.game.screen, BLACK, message_rect.inflate(10, 5))
        self.game.screen.blit(message_surface, message_rect.topleft)
        pygame.display.flip()

    def display_end_message(self, winner, looser):
        self.game.screen.fill(BLACK)
        self.display_message(f"{looser.name} is K.O. !", 50, 200, RED)
        self.display_message(f"{winner.name} gains {looser.giveXp} XP! Total XP: {winner.experience}/{winner.limitXP}", 50, 250, WHITE)
        self.display_message(f"{winner.name} has been updated in players.json", 50, 350, WHITE)
        self.display_message(f"The winner is {winner.name}!", 50, 400, YELLOW)
        pygame.display.flip()
        pygame.time.delay(5000)

    def display_turn(self, attacker_name):
        self.display_message(f"{attacker_name}'s turn to attack!", 300, 400, YELLOW)

    def display_winner(self, winner):
        self.display_message(f"Winner: {winner.name}!", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, YELLOW)
        pygame.time.delay(3000)

    def start_battle(self):
        self.game.run()
