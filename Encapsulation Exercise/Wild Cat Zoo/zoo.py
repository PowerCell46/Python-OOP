from project.vet import Vet

class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self._animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self._workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self._animal_capacity > 0 and self.__budget - price >= 0:
            self._animal_capacity -= 1
            self.__budget -= price
            self.animals.append(animal)
            return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

        elif self.__budget - price < 0:
            return f'Not enough budget'

        elif self._animal_capacity == 0:
            return f'Not enough space for animal'

    def hire_worker(self, worker):
        if self._workers_capacity > 0:
            self._workers_capacity -= 1
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'
        else:
            return f'Not enough space for worker'

    def fire_worker(self, worker_name):
        for index in range(0, len(self.workers)):
            worker = self.workers[index]
            if worker.name == worker_name:
                self.workers.pop(index)
                self._workers_capacity += 1
                return f'{worker_name} fired successfully'

        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        sum_of_salaries = 0
        for worker in self.workers:
            sum_of_salaries += worker.salary
        if self.__budget - sum_of_salaries >= 0:
            self.__budget -= sum_of_salaries
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        else:
            return f'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        sum_of_needed_money = 0
        for animal in self.animals:
            sum_of_needed_money += animal.money_for_care
        if self.__budget - sum_of_needed_money >= 0:
            self.__budget -= sum_of_needed_money
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        else:
            return f'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lion_list = []
        tiger_list = []
        cheetah_list = []
        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lion_list.append(animal.__repr__())
            elif animal.__class__.__name__ == "Tiger":
                tiger_list.append(animal.__repr__())
            elif animal.__class__.__name__ == "Cheetah":
                cheetah_list.append(animal.__repr__())
        final_lions = "\n".join(lion_list)
        final_tigers = "\n".join(tiger_list)
        final_cheetahs = "\n".join(cheetah_list)
        return f'You have {len(self.animals)} animals\n----- {len(lion_list)} Lions:\n{final_lions}\n----- {len(tiger_list)} Tigers:\n{final_tigers}\n----- {len(cheetah_list)} Cheetahs:\n{final_cheetahs}'

    def workers_status(self):
        keepers_list = []
        caretakers_list = []
        vets_list = []
        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers_list.append(worker.__repr__())
            elif worker.__class__.__name__ == "Caretaker":
                caretakers_list.append(worker.__repr__())
            elif worker.__class__.__name__ == "Vet":
                vets_list.append(worker.__repr__())
        final_keepers = "\n".join(keepers_list)
        final_caretakers = "\n".join(caretakers_list)
        final_vets = "\n".join(vets_list)
        return f'You have {len(self.workers)} workers\n----- {len(keepers_list)} Keepers:\n{final_keepers}\n----- {len(caretakers_list)} Caretakers:\n{final_caretakers}\n----- {len(vets_list)} Vets:\n{final_vets}'
