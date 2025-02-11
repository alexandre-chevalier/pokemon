
class combat:
    def __init__(self):
        self.pokemon_disponibles = self.charger_pokemons()
        self.pokedex = self.charger_pokedex()
    
    def charger_pokemons(self):
        try:
            with open("pokemon.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def charger_pokedex(self):
        try:
            with open("pokedex.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def enregistrer_pokedex(self, pokemon):
        if pokemon.nom not in self.pokedex:
            self.pokedex.append(pokemon.nom)
            with open("pokedex.json", "w") as f:
                json.dump(self.pokedex, f, indent=4)
            print(f"{pokemon.nom} ajouté au Pokédex !")
    
    def enregistrer_vainqueur(self, vainqueur):
        with open("vainqueurs.json", "a") as f:
            json.dump({"vainqueur": vainqueur}, f)
            f.write("\n")
    
    def lancer_combat(self, joueur, adversaire):
        print(f"Combat entre {joueur.nom} et {adversaire.nom} !")
        
        while not joueur.est_ko() and not adversaire.est_ko():
            degats_joueur = joueur.calculer_degats(adversaire)
            adversaire.subir_degats(degats_joueur)
            
            if adversaire.est_ko():
                break
            
            degats_adversaire = adversaire.calculer_degats(joueur)
            joueur.subir_degats(degats_adversaire)
        
        vainqueur = joueur.nom if not joueur.est_ko() else adversaire.nom
        self.enregistrer_pokedex(adversaire if adversaire.est_ko() else joueur)
        self.enregistrer_vainqueur(vainqueur)
        print(f"Le vainqueur est {vainqueur} !")
    
    def ajouter_pokemon(self):
        nom = input("Nom du Pokémon : ")
        type = input("Type : ")
        pv = int(input("Points de vie : "))
        attaque = int(input("Attaque : "))
        defense = int(input("Défense : "))
        
        nouveau_pokemon = {"nom": nom, "type": type, "pv": pv, "attaque": attaque, "defense": defense}
        self.pokemon_disponibles.append(nouveau_pokemon)
        
        with open("pokemon.json", "w") as f:
            json.dump(self.pokemon_disponibles, f, indent=4)
        print(f"{nom} a été ajouté !")
    
    def acceder_pokedex(self):
        try:
            with open("pokedex.json", "r") as f:
                print(json.load(f))
        except FileNotFoundError:
            print("Aucun Pokémon enregistré dans le Pokédex.")