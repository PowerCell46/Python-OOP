from project.animals.animal import Bird


class Owl(Bird):
    def make_sound(self):
        return f'Hoot Hoot'

    def feed(self, food):
        if food.__class__.__name__ == "Meat":
            self.food_eaten += 1 * food.quantity
            self.weight += 0.25 * food.quantity
        else:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'


class Hen(Bird):
    def make_sound(self):
        return f'Cluck'

    def feed(self, food):
        self.food_eaten += 1 * food.quantity
        self.weight += 0.35 * food.quantity


