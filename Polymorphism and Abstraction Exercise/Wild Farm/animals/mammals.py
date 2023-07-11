from project.animals.animal import Mammal


class Mouse(Mammal):
    def make_sound(self):
        return f'Squeak'

    def feed(self, food):
        if food.__class__.__name__ == "Vegetable" or food.__class__.__name__ == "Fruit":
            self.food_eaten += 1 * food.quantity
            self.weight += 0.10 * food.quantity
        else:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'


class Dog(Mammal):
    def make_sound(self):
        return f'Woof!'

    def feed(self, food):
        if food.__class__.__name__ == "Meat":
            self.food_eaten += 1 * food.quantity
            self.weight += 0.40 * food.quantity
        else:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'


class Cat(Mammal):
    def make_sound(self):
        return f'Meow'

    def feed(self, food):
        if food.__class__.__name__ == "Vegetable" or food.__class__.__name__ == "Meat":
            self.food_eaten += 1 * food.quantity
            self.weight += 0.30 * food.quantity
        else:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'


class Tiger(Mammal):
    def make_sound(self):
        return f'ROAR!!!'

    def feed(self, food):
        if food.__class__.__name__ == "Meat":
            self.food_eaten += 1 * food.quantity
            self.weight += 1 * food.quantity
        else:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
