from project.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8

    def __init__(self, fuel, horsepower):
        super().__init__(fuel, horsepower)
        self.fuel_consumption = 8
