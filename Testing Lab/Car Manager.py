import unittest
# from CarManager.car_manager import Car


class TestCar(unittest.TestCase):
    def setUp(self):
        self.my_car = Car("Meet your maker", "Audi A8", 10, 100)

    def test_the_init_method(self):
        self.assertEqual(self.my_car.make, "Meet your maker")
        self.assertEqual(self.my_car.model, "Audi A8")
        self.assertEqual(self.my_car.fuel_consumption, 10)
        self.assertEqual(self.my_car.fuel_capacity, 100)
        self.assertEqual(self.my_car.fuel_amount, 0)

    def test_make_with_empty_string(self):
        with self.assertRaises(Exception) as ex:
            self.my_car.make = ""
        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def test_make_with_None(self):
        with self.assertRaises(Exception) as ex:
            self.my_car.make = None
        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def test_model_with_empty_string(self):
        with self.assertRaises(Exception) as ex:
            self.my_car.model = ""
        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_model_with_None(self):
        with self.assertRaises(Exception) as ex:
            self.my_car.model = None
        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_fuel_consumption_with_0(self):
        with self.assertRaises(Exception) as ex:
            self.my_car.fuel_consumption = 0
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_consumption_with_negative_value(self):
        with self.assertRaises(Exception) as ex:
            self.my_car.fuel_consumption = -1
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def testing_fuel_capacity_with_0(self):
        with self.assertRaises(Exception) as ex:
            self.my_car.fuel_capacity = 0
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

    def testing_fuel_capacity_with_negative_number(self):
        with self.assertRaises(Exception) as ex:
            self.my_car.fuel_capacity = -1
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

    def testing_fuel_amount_with_zero(self):
        self.my_car.fuel_amount = 0
        self.assertEqual(self.my_car.fuel_amount, 0)

    def testing_fuel_amount_with_negative_number(self):
        with self.assertRaises(Exception) as ex:
            self.my_car.fuel_amount = -1
        self.assertEqual(str(ex.exception), "Fuel amount cannot be negative!")

    def testing_the_refuel_method_with_correct_data(self):
        self.my_car.refuel(10)
        self.assertEqual(self.my_car.fuel_amount, 10)

    def testing_the_refuel_method_with_too_much_fuel(self):
        self.my_car.refuel(120)
        self.assertEqual(self.my_car.fuel_amount, 100)

    def testing_the_refuel_with_0(self):
        with self.assertRaises(Exception) as ex:
            self.my_car.refuel(0)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def testing_the_refuel_with_negative_value(self):
        with self.assertRaises(Exception) as ex:
            self.my_car.refuel(-1)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def testing_the_drive_method_with_just_enough_fuel(self):
        self.my_car.refuel(10)
        self.my_car.drive(100)
        self.assertEqual(self.my_car.fuel_amount, 0)

    def testing_the_drive_method_with_left_out_fuel(self):
        self.my_car.refuel(20)
        self.my_car.drive(100)
        self.assertEqual(self.my_car.fuel_amount, 10)

    def testing_the_drive_method_with_not_enough_fuel(self):
        self.my_car.refuel(5)
        with self.assertRaises(Exception) as ex:
            self.my_car.drive(1000)
        self.assertEqual(str(ex.exception), "You don't have enough fuel to drive!")


if __name__ == '__main__':
    unittest.main()
