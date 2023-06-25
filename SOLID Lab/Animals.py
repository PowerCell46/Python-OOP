class Animal:
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species


def animal_sound(animals: list):
    for animal in animals:
        if animal.species == 'cat':
            print('meow')
        elif animal.species == 'dog':
            print('woof-woof')
        elif animal.species == 'chicken':
            print(f'cluck')
        else:
            print(f'Animal noise...')


animals = [Animal('cat'), Animal('dog')]
animal_sound(animals)

animals2 = [Animal('cat'), Animal('dog'), Animal('chicken')]
animal_sound(animals2)
