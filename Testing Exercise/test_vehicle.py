import unittest
from project.vehicle import Vehicle

class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.my_vehicle = Vehicle(100, 400)

    def test_the_init(self):
        self.assertEqual(self.my_vehicle.fuel, 100)
        self.assertEqual(self.my_vehicle.capacity, 100)
        self.assertEqual(self.my_vehicle.horse_power, 400)
        self.assertEqual(self.my_vehicle.fuel_consumption, 1.25)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, 1.25)

    def testing_the_drive_method(self):
        self.my_vehicle.drive(80)
        self.assertEqual(self.my_vehicle.fuel, 0)

    def testing_the_drive_method_with_not_enough_fuel(self):
        with self.assertRaises(Exception) as context:
            self.my_vehicle.drive(120)
        self.assertEqual(str(context.exception), "Not enough fuel")

    def test_refuel_with_possible_quantity(self):
        self.my_vehicle.drive(10)
        self.my_vehicle.refuel(10)
        self.assertEqual(self.my_vehicle.fuel, 97.5)

    def test_refuel_with_too_much(self):
        self.my_vehicle.drive(10)
        with self.assertRaises(Exception) as context:
            self.my_vehicle.refuel(25)
        self.assertEqual(str(context.exception), "Too much fuel")

    def testing_the_string_method(self):
        self.assertEqual(self.my_vehicle.__str__(), "The vehicle has 400 horse power with 100 fuel left and 1.25 fuel consumption")

if __name__ == "__main__":
    unittest.main()