import pygame
import random
import json
import os
from pokemon import Pokemon
from player import Player


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


BASE_DIR = r"C:\Users\ndiay\Desktop\lptf\projets\pokemon\develop"
IMAGE_DIR = os.path.join(BASE_DIR, "images")
SOUND_DIR = os.path.join(BASE_DIR, "sounds")


font_path = os.path.join(BASE_DIR,"Audiowide-Regular.ttf")
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


    def __init__(self,player):
        self.player = player
        self.pokemon1 = self.load_player_pokemon()
        pokemon_list = self.load_pokemon_list()
        self.pokemon2 = (random.choice(pokemon_list)) 
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pokemon Battle")
        self.attack_button_rect = None

        # Load
        # Pokémon images
        self.pokemon1_image = self.load_and_scale_image(self.pokemon1.name, (150, 150))
        self.pokemon2_image = self.load_and_scale_image(self.pokemon2.name, (150, 150))
    
    def load_player_pokemon(self):
        """Charge le Pokémon actif du joueur depuis 'players.json'"""
        try:
            with open('players.json', 'r') as file:
                data = json.load(file)

                if not data:
                    raise ValueError("Le fichier players.json est vide !")

                player = data[0]  # On suppose qu'il y a un seul joueur
                player_name = player["name"]  
                pokemon_data = player.get("pokemon", {})

                # Liste des attributs attendus pour créer un Pokémon
                expected_keys = {"name", "lifePoint", "level", "XP", "giveXP", "limitXP", "attack", "defence", "type1", "type2", "next_evolution"}
                filtered_data = {k: v for k, v in pokemon_data.items() if k in expected_keys}

                return Pokemon(**filtered_data)

        except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
            print(f"Erreur lors du chargement du Pokémon du joueur: {e}")
        return None, None

                
        

    
    def load_pokemon_list(self):
        try:
          with open('pokemon.json', 'r') as file:
            data = json.load(file)
            # Liste des attributs attendus dans la classe Pokemon
            expected_keys = {"name","lifePoint", "level", "XP", "giveXP", "limitXP",  "attack", "defence", "type1", "type2", "next_evolution"}
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

        # Display Pokemon 2 characteristics
        pokemon2_info = font.render(
            f"{self.pokemon2.name} - HP: {self.pokemon2.lifePoint}, Attack: {self.pokemon2.attack}, Defense: {self.pokemon2.defence}, Type: {self.pokemon2.type1}",
            True, WHITE
        )
        self.screen.blit(pokemon2_info, (50, 100))

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
    
    def attack(self, attacker, target):
        self.play_attack_sound() 
        multiplier = self.calculate_multiplier(attacker, target)
        damage = max(0, (attacker.attack * multiplier) - target.defence)
        target.lifePoint -= damage
        print(f"{attacker.name} attacks {target.name} with a multiplier of {multiplier}. Damage dealt: {damage}")
         
        # Display damage on screen
        damage_text = font.render(f"{attacker.name} deals {damage} damage to {target.name}!", True, RED)
        self.screen.blit(damage_text, (50, 300))

        if target.lifePoint <= 0:
            target.KO = True
            print(f"{target.name} is K.O. !")

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
        
    def record_in_pokedex(self, pokemon):
        try:
         if not hasattr(self, "pokedex"):
             self.pokedex = []
             if os.path.exists("pokedex.json"):
                 with open("pokedex.json", "r") as f:
                     self.pokedex = json.load(f)
         
         if pokemon.name not in self.pokedex:
             self.pokedex.append(pokemon.name)
             with open("pokedex.json", "w") as f:
                 json.dump(self.pokedex, f, indent=4)
             print(f"{pokemon.name} ajouté au Pokédex !")
        except Exception as e:
         print(f"Erreur lors de l'ajout au Pokédex : {e}")
    
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
        print(f"{winner.name} monte au niveau {winner.level} !")

    # Sauvegarder les nouvelles stats du gagnant dans players.json
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

    # Ajouter au fichier vainqueurs.json
        with open("vainqueurs.json", "a") as f:
            json.dump({"vainqueur": winner.name}, f)
            f.write("\n")  
   
    def display_end_message(self, winner, looser):
        self.screen.fill(BLACK)
        message1 = font.render(f"{looser.name} is K.O. !", True, RED)
        message2 = font.render(f"{winner.name} gagne {looser.giveXp} XP ! XP total: {winner.experience}/{winner.limitXP}", True, WHITE)
        message3 = font.render(f"{winner.name} monte au niveau {winner.level} !", True, YELLOW)
        message4 = font.render(f"{winner.name} a été mis à jour dans players.json", True, WHITE)
        message5 = font.render(f"The winner is {winner.name}!", True, YELLOW)
        
        self.screen.blit(message1, (50, 200))
        self.screen.blit(message2, (50, 250))
        self.screen.blit(message3, (50, 300))
        self.screen.blit(message4, (50, 350))
        self.screen.blit(message5, (50, 400))
        
        pygame.display.flip()
        pygame.time.delay(5000)
    def start_battle(self):
        running = True
        turn = 1  # 1 for Pokemon1's turn, 2 for Pokemon2's turn

        while running:
            self.screen.fill(BLACK)
            self.display_characteristics()
            self.draw_attack_button()

            # Display whose turn it is
            if turn == 1:
                self.display_turn(self.pokemon1.name)
            else:
                self.display_turn(self.pokemon2.name)

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
                self.display_winner(winner) # Affichage du gagnant
                self.record_in_pokedex(self.pokemon2)
                self.record_winner(winner,looser)
                self.display_end_message(winner, looser)

                print(f"The winner is {winner.name}!")
                
                running = False

            pygame.display.flip()

        pygame.quit()

# Example usage
player = Player('C:/Users/ndiay/Desktop/lptf/projets/pokemon/pokemon.json', 'C:/Users/ndiay/Desktop/lptf/projets/pokemon/players.json')

player.save_to_file(os.path.join(BASE_DIR, "players.json"))
combat = Combat(player)
combat.start_battle()