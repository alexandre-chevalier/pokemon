from player import Player
from combat import Combat
import pygame


pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 223, 0)

def main():
    
    player_name = Player.ask_for_name()
    player = Player(player_name)

    chosen_pokemon = player.display_pokemon_list()

    if chosen_pokemon:
        player.pokemon = chosen_pokemon
        player.save_to_file()
        print(f"Le joueur {player_name} a choisi {chosen_pokemon['name']} et a été enregistré.")

        combat = Combat(player)

        combat.start_battle()
    else:
        print("Aucun Pokémon n'a été choisi.")

if __name__ == "__main__":
    main()
