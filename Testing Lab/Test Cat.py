import unittest

class CatTests(unittest.TestCase):
    def setUp(self):
        self.animal = Cat("Meow")

    def test_name(self):
        self.assertEqual(self.animal.name, "Meow")
        self.assertEqual(self.animal.fed, False)
        self.assertEqual(self.animal.size, 0)
        self.assertEqual(self.animal.sleepy, False)

    def test_eating_while_fed(self):
        self.animal.fed = True
        with self.assertRaises(Exception) as context:
            self.animal.eat()
        self.assertEqual(str(context.exception), "Already fed.")

    def test_eating(self):
        self.animal.eat()
        self.assertEqual(self.animal.sleepy, True)
        self.assertEqual(self.animal.fed, True)
        self.assertEqual(self.animal.size, 1)

    def test_sleeping_while_not_fed(self):
        self.animal.fed = False
        with self.assertRaises(Exception) as context:
            self.animal.sleep()
        self.assertEqual(str(context.exception), "Cannot sleep while hungry")

    def test_sleeping(self):
        self.animal.eat()
        self.assertEqual(self.animal.sleepy, True)
        self.animal.sleep()
        self.assertEqual(self.animal.sleepy, False)

if __name__ == "__main__":
    unittest.main()
