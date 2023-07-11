from abc import abstractmethod, ABC


class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        ...

    @abstractmethod
    def refuel(self):
        ...


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity  # per km
        self.fuel_consumption = fuel_consumption  # per km

    def drive(self, distance):
        if self.fuel_quantity >= (self.fuel_consumption + 0.9) * distance:
            self.fuel_quantity -= (self.fuel_consumption + 0.9) * distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if self.fuel_quantity >= (self.fuel_consumption + 1.6) * distance:
            self.fuel_quantity -= (self.fuel_consumption + 1.6) * distance

    def refuel(self, fuel):
        self.fuel_quantity += ((fuel / 100) * 95)
