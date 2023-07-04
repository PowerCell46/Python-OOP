from project.car import Car
from project.vehicle import Vehicle

class SportsCar(Car):
    def race(self):
        return f'racing...'

# my_bugatti = SportsCar()
# print(my_bugatti.move())