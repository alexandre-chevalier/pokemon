import pygame
import random
import json
import os
from pokemon import Pokemon
from player import Player
from battle_manager import BattleManager

# Initialize Pygame
pygame.init()
pygame.font.init()

# Screen size
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 223, 0)

BASE_DIR = r"C:/Users/Windows/Desktop/projets/1a/pokemon"
IMAGE_DIR = os.path.join(BASE_DIR, "images")
SOUND_DIR = os.path.join(BASE_DIR, "sounds")

font_path = os.path.join(BASE_DIR, "Audiowide-Regular.ttf")
font = pygame.font.Font(font_path, 36)

file_path = os.path.join(BASE_DIR, "players.json")

class SpecialMove:
    def __init__(self, name, damage, accuracy, effect=None):
        self.name = name
        self.damage = damage
        self.accuracy = accuracy
        self.effect = effect

    def apply_effect(self, target):
        if self.effect and random.random() < self.effect.get('chance', 1.0):
            status = self.effect.get('status')
            duration = self.effect.get('duration', 3)  # Default duration of 3 turns
            if status:
                target.add_status_effect(status, duration)
                print(f"{target.name} is affected by {status} for {duration} turns!")

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

    def __init__(self, player, battle_manager=None):
        self.player = player
        self.battle_manager = battle_manager if battle_manager else BattleManager(file_path)
        pokemon_list = self.load_pokemon_list()
        self.pokemon2 = random.choice(pokemon_list)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pokemon Battle")
        self.attack_button_rect = None
        self.player_name, self.pokemon1 = self.load_player_pokemon()
        if self.pokemon1 is None:
            raise ValueError("Erreur lors du chargement du Pokémon du joueur.")
        self.pokemon1_image = self.load_and_scale_image(self.pokemon1.name, (150, 150))
        self.pokemon2_image = self.load_and_scale_image(self.pokemon2.name, (150, 150))
        # Define special moves for demonstration
        self.special_moves = [
            SpecialMove("Fire Blast", 50, 0.85, {"status": "burn", "chance": 0.3, "duration": 5}),
            SpecialMove("Thunderbolt", 45, 0.9, {"status": "paralysis", "chance": 0.2, "duration": 4}),
            SpecialMove("Ice Beam", 40, 0.95, {"status": "freeze", "chance": 0.1, "duration": 3}),
        ]

    def apply_status_effects(self, pokemon):
        pokemon.decrement_status_effects()
        for effect, duration in pokemon.status_effects.items():
            if effect == "burn":
                pokemon.lifePoint -= 5
                print(f"{pokemon.name} is hurt by burn!")
            elif effect == "paralysis" and random.random() < 0.5:
                print(f"{pokemon.name} is paralyzed and can't move!")
                return True  # Pokémon can't move this turn
            elif effect == "freeze" and random.random() < 0.2:
                print(f"{pokemon.name} is frozen solid!")
                return True  # Pokémon can't move this turn
        return False

    def display_status_effects(self, pokemon, x, y):
        if pokemon.status_effects:
            effects_text = ", ".join(pokemon.status_effects.keys())
            status_text = font.render(f"Status: {effects_text}", True, YELLOW)
            self.screen.blit(status_text, (x, y))

    def load_player_pokemon(self):
        """Charge le Pokémon actif du joueur depuis 'players.json'"""
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)

                if not data:
                    raise ValueError("Le fichier players.json est vide !")

                player = data[0]  # On suppose qu'il y a un seul joueur
                player_name = player["name"]
                pokemon_data = player.get("pokemon", {})

                # Liste des attributs attendus pour créer un Pokémon
                expected_keys = {"name", "lifePoint", "level", "XP", "giveXP", "limitXP", "attack", "defence", "type1", "type2", "next_evolution"}
                filtered_data = {k: v for k, v in pokemon_data.items() if k in expected_keys}
                print(f"Nom du joueur : {player_name}")

                return player_name, Pokemon(**filtered_data)

        except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
            print(f"Erreur lors du chargement du Pokémon du joueur: {e}")
        return None, None

    def load_pokemon_list(self):
        try:
            with open(os.path.join(BASE_DIR, 'pokemon.json'), 'r') as file:
                data = json.load(file)
                # Liste des attributs attendus dans la classe Pokemon
                expected_keys = {"name", "lifePoint", "level", "XP", "giveXP", "limitXP", "attack", "defence", "type1", "type2", "next_evolution"}
                # Filtrer uniquement les clés valides
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

    def display_characteristics(self):
        # Display Pokemon 1 characteristics
        pokemon1_info = font.render(
            f"{self.pokemon1.name} - HP: {self.pokemon1.lifePoint}, Attack: {self.pokemon1.attack}, Defense: {self.pokemon1.defence}, Type: {self.pokemon1.type1}",
            True, WHITE
        )
        self.screen.blit(pokemon1_info, (50, 50))
        self.display_status_effects(self.pokemon1, 50, 80)

        # Display Pokemon 2 characteristics
        pokemon2_info = font.render(
            f"{self.pokemon2.name} - HP: {self.pokemon2.lifePoint}, Attack: {self.pokemon2.attack}, Defense: {self.pokemon2.defence}, Type: {self.pokemon2.type1}",
            True, WHITE
        )
        self.screen.blit(pokemon2_info, (50, 150))
        self.display_status_effects(self.pokemon2, 50, 180)

        # Display Pokémon images
        if self.pokemon1_image:
            self.screen.blit(self.pokemon1_image, (50, 200))
        if self.pokemon2_image:
            self.screen.blit(self.pokemon2_image, (SCREEN_WIDTH - 200, 200))

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

        if not move:
            move = random.choice(self.special_moves)

        if random.random() < move.accuracy:
            multiplier = self.calculate_multiplier(attacker, target)
            damage = max(0, (attacker.attack * multiplier * move.damage / 100) - target.defence)
            target.lifePoint -= damage
            print(f"{attacker.name} uses {move.name} on {target.name} with a multiplier of {multiplier}. Damage dealt: {damage}")
            move.apply_effect(target)

            # Display damage on screen
            damage_text = font.render(f"{attacker.name} deals {damage} damage to {target.name}!", True, RED)
            self.screen.blit(damage_text, (50, 300))

            if target.lifePoint <= 0:
                target.KO = True
                print(f"{target.name} is K.O. !")
        else:
            print(f"{attacker.name}'s attack missed!")

    def draw_attack_button(self):
        button_width = 200
        button_height = 50
        self.attack_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT - button_height - 20, button_width, button_height)
        pygame.draw.rect(self.screen, YELLOW, self.attack_button_rect, border_radius=10)

        # Button text
        attack_button_text = font.render("Attack", True, BLACK)
        attack_button_text_rect = attack_button_text.get_rect(center=self.attack_button_rect.center)
        self.screen.blit(attack_button_text, attack_button_text_rect)

    def display_turn(self, attacker_name):
        turn_info = font.render(f"{attacker_name}'s turn to attack!", True, WHITE)
        self.screen.blit(turn_info, (50, 150))

    def display_winner(self, winner):
        winner_text = font.render(f"Winner: {winner.name}!", True, YELLOW)
        self.screen.blit(winner_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(3000)

    def get_pokedex_list(self):
        try:
            with open(os.path.join(BASE_DIR, 'poke.json'), 'r', encoding='utf-8') as file:
                # Lire le contenu du fichier
                contenu = file.read().strip()
                # Si le fichier est vide ou ne contient que des espaces, réinitialiser
                if not contenu:
                    raise ValueError("Le fichier est vide")
                self.pokedex_list = json.loads(contenu)
        except (FileNotFoundError, ValueError, json.JSONDecodeError):
            print("Le fichier poke.json est vide ou invalide. Réinitialisation...")
            self.pokedex_list = []
            # Réinitialisation du fichier poke.json avec une liste vide
            with open(os.path.join(BASE_DIR, 'poke.json'), 'w', encoding='utf-8') as file:
                json.dump(self.pokedex_list, file, indent=4)

        return self.pokedex_list

    def record_pokedex(self, pokemon):
        # Vérifier que la liste des Pokémon a bien été chargée
        self.get_pokedex_list()

        if not self.player:  # Vérifier si le joueur est défini
            return

        player_name = self.player.name  # Convertir l'objet Player en chaîne
        player_found = False

        # Parcourir les entrées du Pokédex
        for entry in self.pokedex_list:
            if player_name in entry:  # Chercher l'entrée du joueur par nom
                pokemon_dict = entry[player_name]

                # Si le Pokémon est déjà présent, mettre à jour ses données
                if pokemon.name in pokemon_dict:
                    pokemon_dict[pokemon.name]["count"] += 1
                else:
                    # Ajouter toutes les informations du Pokémon
                    pokemon_dict[pokemon.name] = {
                        "count": 1,
                        "lifePoint": pokemon.lifePoint,
                        "level": pokemon.level,
                        "attack": pokemon.attack,
                        "defence": pokemon.defence,
                        "type1": pokemon.type1,
                        "type2": pokemon.type2,
                    }

                # Mettre à jour l'entrée du joueur avec les nouvelles données du Pokémon
                entry[player_name] = pokemon_dict
                player_found = True
                break

        # Si l'entrée du joueur n'a pas été trouvée, créer une nouvelle entrée
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

        # Sauvegarder les données du Pokédex dans le fichier poke.json
        try:
            with open(os.path.join(BASE_DIR, 'poke.json'), 'w', encoding='utf-8') as file:
                json.dump(self.pokedex_list, file, indent=4, ensure_ascii=False)
            print("Données enregistrées dans poke.json")
        except Exception as e:
            print(f"Erreur lors de l'enregistrement dans poke.json: {e}")

    def record_winner(self, winner, looser):
        # Augmenter l'XP du Pokémon gagnant
        winner.experience += looser.giveXp
        print(f"{winner.name} gagne {looser.giveXp} XP ! XP total: {winner.experience}/{winner.limitXP}")

        # Vérifier s'il passe au niveau suivant
        if winner.experience >= winner.limitXP:
            winner.level += 1
            winner.XP -= winner.limitXP
            winner.limitXP *= 3
            winner.attack += 2
            winner.defence += 2
            #print(f"{winner.name} monte au niveau {winner.level} !")
            message3 = font.render(f"{winner.name} monte au niveau {winner.level} !", True, YELLOW)
            self.screen.blit(message3, (50, 300))

        # Sauvegarder les nouvelles stats du gagnant dans players.json
        self.battle_manager.record_winner(winner, looser)

        # Supprimer le Pokémon perdant de l'équipe du joueur
        self.battle_manager.remove_loser_pokemon(looser)

    def display_end_message(self, winner, looser):
        self.screen.fill(BLACK)
        message1 = font.render(f"{looser.name} is K.O. !", True, RED)
        message2 = font.render(f"{winner.name} gagne {looser.giveXp} XP ! XP total: {winner.experience}/{winner.limitXP}", True, WHITE)

        message4 = font.render(f"{winner.name} a été mis à jour dans players.json", True, WHITE)
        message5 = font.render(f"The winner is {winner.name}!", True, YELLOW)

        self.screen.blit(message1, (50, 200))
        self.screen.blit(message2, (50, 250))
        self.screen.blit(message4, (50, 350))
        self.screen.blit(message5, (50, 400))

        pygame.display.flip()
        pygame.time.delay(5000)

    def start_battle(self):
        running = True
        turn = 1  # 1 for Pokemon1's turn, 2 for Pokemon2's turn

        while running:
            self.screen.fill(BLACK)  # Clear the screen
            self.display_characteristics()
            self.draw_attack_button()

            # Display whose turn it is
            if turn == 1:
                self.display_turn(self.pokemon1.name)
                if self.apply_status_effects(self.pokemon1):
                    turn = 2  # Skip turn if paralyzed or frozen
            else:
                self.display_turn(self.pokemon2.name)
                if self.apply_status_effects(self.pokemon2):
                    turn = 1  # Skip turn if paralyzed or frozen

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.attack_button_rect.collidepoint(event.pos):
                        if turn == 1:
                            self.attack(self.pokemon1, self.pokemon2)
                            turn = 2
                        else:
                            self.attack(self.pokemon2, self.pokemon1)
                            turn = 1

            if self.pokemon1.KO or self.pokemon2.KO:
                winner = self.pokemon1 if not self.pokemon1.KO else self.pokemon2
                looser = self.pokemon1 if self.pokemon1.KO else self.pokemon2
                self.display_winner(winner)
                self.record_pokedex(self.pokemon2)
                self.record_winner(winner, looser)
                self.display_end_message(winner, looser)

                print(f"The winner is {winner.name}!")
                running = False

            pygame.display.flip()

        pygame.quit()

player = Player(os.path.join(BASE_DIR, 'pokemon.json'), os.path.join(BASE_DIR, 'players.json'))

# Vérifier si le fichier poke.json est vide ou mal formé
poke_file_path = os.path.join(BASE_DIR, 'poke.json')
if os.path.exists(poke_file_path):
    with open(poke_file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
            print(json.dumps(data, indent=4, ensure_ascii=False))  # Affiche bien formaté
        except json.JSONDecodeError:
            print("Le fichier poke.json est vide ou mal formé. Réinitialisation...")
            data = []
            with open(poke_file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
else:
    print("Le fichier poke.json n'existe pas. Création d'un nouveau fichier...")
    data = []
    with open(poke_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

player.save_to_file(file_path)
combat = Combat(player)
combat.start_battle()
