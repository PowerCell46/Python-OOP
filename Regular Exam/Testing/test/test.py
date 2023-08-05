from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):
    def testInitMethod(self):
        instance = SecondHandCar("Audi A8", "Sport's car", 100_000, 10_000)
        self.assertEqual(instance.price, 10_000)
        self.assertEqual(instance.model, "Audi A8")
        self.assertEqual(instance.car_type, "Sport's car")
        self.assertEqual(instance.mileage, 100_000)
        self.assertEqual(instance.repairs, [])

    def testPriceWith1point1(self):
        instance = SecondHandCar("Audi A7", "Sports car", 100_000, 1.1)
        self.assertEqual(instance.price, 1.1)

    def testPriceWith1(self):
        with self.assertRaises(ValueError) as err:
            instance = SecondHandCar("Audi A7", "Sports car", 100_000, 1)
        self.assertEqual("Price should be greater than 1.0!", str(err.exception))

    def testPriceWith0(self):
        with self.assertRaises(ValueError) as err:
            instance = SecondHandCar("Audi A7", "Sports car", 100_000, 0)
        self.assertEqual("Price should be greater than 1.0!", str(err.exception))

    def testMileageWith101(self):
        instance = SecondHandCar("Audi A7", "Sports car", 101, 1_000)
        self.assertEqual(instance.mileage, 101)

    def testMileageWith100(self):
        with self.assertRaises(ValueError) as err:
            instance = SecondHandCar("Audi A7", "Sports car", 100, 100_000)
        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(err.exception))

    def testMileageWith99(self):
        with self.assertRaises(ValueError) as err:
            instance = SecondHandCar("Audi A8", "Sports car", 99, 100_000)
        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(err.exception))

    def testSetPromotionalPriceWithTheSameValue(self):
        with self.assertRaises(ValueError) as err:
            instance = SecondHandCar("Audi A8", "Sports car", 1_000, 10_000)
            instance.set_promotional_price(10_000)
        self.assertEqual("You are supposed to decrease the price!", str(err.exception))

    def testSetPromotionalPriceWithBiggerValue(self):
        with self.assertRaises(ValueError) as err:
            instance = SecondHandCar("Audi A8", "Sports car", 1_000, 10_000)
            instance.set_promotional_price(100_000)
        self.assertEqual("You are supposed to decrease the price!", str(err.exception))

    def testSetPromotionalPriceWithSmallerValue(self):
        instance = SecondHandCar("Audi A8", "Sports car", 1_000, 10_000)
        self.assertEqual(instance.set_promotional_price(8_000), "The promotional price has been successfully set.")
        self.assertEqual(instance.price, 8_000)

    def testNeedRepairWithPriceBigger(self):
        instance = SecondHandCar("Audi A8", "Sports car", 1_000, 10_000)
        self.assertEqual(instance.need_repair(6_000, "Сменяне на ауспуха."), "Repair is impossible!")

    def testNeedRepairWithSamePrice(self):
        instance = SecondHandCar("Audi A8", "Sports car", 1_000, 10_000)
        self.assertEqual(instance.need_repair(5_000, "Сменяне на ауспуха."), "Price has been increased due to repair charges.")
        self.assertEqual(instance.price, 15_000)
        self.assertEqual(instance.repairs, ["Сменяне на ауспуха."])

    def testNeedRepairWithSmallerPrice(self):
        instance = SecondHandCar("Audi A8", "Sports car", 1_000, 10_000)
        self.assertEqual(instance.need_repair(1_000, "Сменяне на джантите."), "Price has been increased due to repair charges.")
        self.assertEqual(instance.price, 11_000)
        self.assertEqual(instance.repairs, ["Сменяне на джантите."])

    def testGreaterThanMethodWithDifferentTypes(self):
        first = SecondHandCar("Audi A8", "Sports car", 10_000, 10_000)
        second = SecondHandCar("BMW X5", "Jeep", 10_00, 12_000)
        self.assertEqual(first.__gt__(second), "Cars cannot be compared. Type mismatch!")

    def testGraterThanMethodWithEqualTypes1(self):
        first = SecondHandCar("Audi A8", "Sports car", 10_000, 15_000)
        second = SecondHandCar("BMW", "Sports car", 10_00, 12_000)
        self.assertEqual(first.__gt__(second), True)

    def testGraterThanMethodWithEqualTypes2(self):
        first = SecondHandCar("Audi A8", "Sports car", 10_000, 10_000)
        second = SecondHandCar("BMW", "Sports car", 10_00, 12_000)
        self.assertEqual(first.__gt__(second), False)

    def testStringMethod(self):
        instance = SecondHandCar("BMW X6", "Jeep", 50_000, 18_000)
        instance.need_repair(1_000, "Сменяне на тапицерията.")
        instance.need_repair(2_000, "Годишна проверка и сменяне на маслото.")
        self.assertEqual(str(instance), f'Model BMW X6 | Type Jeep | Milage 50000km\nCurrent price: 21000.00 | Number of Repairs: 2')

if __name__ == "__main__":
    main()