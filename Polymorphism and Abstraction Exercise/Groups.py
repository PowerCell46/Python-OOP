class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f'{self.name} {self.surname}'

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name: str, people: list):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):

        new_name = f'{self.name} {other.name}'
        new_people = []
        new_people.extend(self.people)
        new_people.extend(other.people)

        return Group(new_name, new_people)

    def __repr__(self):
        names = []
        for person in self.people:
            names.append(person.__repr__())
        return f'Group {self.name} with members {", ".join(names)}'

    def __getitem__(self, index):
        return f'Person {index}: {self.people[index]}'

    def __iter__(self):
        return iter([f"Person {self.people.index(person)}: {person}" for person in self.people])
