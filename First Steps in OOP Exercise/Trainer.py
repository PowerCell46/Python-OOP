from project.pokemon import Pokemon

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []
        self.pokemon_names = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemons:
            return f'This pokemon is already caught'
        else:
            self.pokemons.append(pokemon)
            self.pokemon_names.append(pokemon.name)
            return f'Caught {pokemon.name} with health {pokemon.health}'

    def release_pokemon(self, pokemon_name):
        if pokemon_name in self.pokemon_names:
            search_index = self.pokemon_names.index(pokemon_name)
            self.pokemons.pop(search_index)
            self.pokemon_names.pop(search_index)
            return f'You have released {pokemon_name}'
        else:
            return f'Pokemon is not caught'

    def trainer_data(self):
        return_list = []
        for pokemon in self.pokemons:
            return_list.append("- " + pokemon.pokemon_details())
        return_str = "\n".join(return_list)
        return f'Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n{return_str}'
