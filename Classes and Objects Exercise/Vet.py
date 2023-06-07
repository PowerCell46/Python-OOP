class Vet:
    animals = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name):
        if Vet.space > 0:
            Vet.space -= 1
            Vet.animals.append(animal_name)
            self.animals.append(animal_name)
            return f'{animal_name} registered in the clinic'
        return f'Not enough space'

    def unregister_animal(self, animal_name):
        if animal_name in Vet.animals:
            search_index = Vet.animals.index(animal_name)
            Vet.animals.pop(search_index)
            search_index_2 = self.animals.index(animal_name)
            self.animals.pop(search_index_2)
            Vet.space += 1
            return f'{animal_name} unregistered successfully'
        return f'{animal_name} not in the clinic'

    def info(self):
        return f'{self.name} has {len(self.animals)} animals. {Vet.space} space left in the clinic'
