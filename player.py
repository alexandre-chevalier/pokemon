from pokemon import Pokemon

class Player:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if len(self.pokemons) < 6:
            if isinstance(pokemon, Pokemon):
                self.pokemons.append(pokemon)
            else:
                print("Only instances of Pokemon can be added.")
        else:
            print("You can only have a maximum of 6 Pokémon in your team.")

    def remove_pokemon(self, pokemon_name):
        self.pokemons = [pokemon for pokemon in self.pokemons if pokemon.name != pokemon_name]

    def choose_pokemon(self, pokemon_name):
        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name:
                return pokemon
        print(f"No Pokémon named {pokemon_name} found in your team.")
        return None

    def display_team(self):
        print(f"{self.name}'s Pokémon Team:")
        for pokemon in self.pokemons:
            print(pokemon)

    def __str__(self):
        return f"Player: {self.name}, Pokemons: {[pokemon.name for pokemon in self.pokemons]}"

# Example usage
if __name__ == "__main__":
    player = Player("Ash")
    pikachu = Pokemon("Pikachu", 100, 1, 0, 10, 20, 10, 8, "electric", None, None)
    charmander = Pokemon("Charmander", 100, 1, 0, 10, 20, 10, 8, "fire", None, None)

    player.add_pokemon(pikachu)
    player.add_pokemon(charmander)
    player.display_team()
    chosen_pokemon = player.choose_pokemon("Pikachu")
    if chosen_pokemon:
        print(f"Chosen Pokémon: {chosen_pokemon.name}")
    print(player)