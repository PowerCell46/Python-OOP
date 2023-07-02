import unittest
from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self):
        self.my_mammal = Mammal("Human", "Human-type", 'speak')

    def test_make_sound(self):
        self.assertEqual(self.my_mammal.make_sound(), "Human makes speak")
        self.assertEqual(self.my_mammal.sound, "speak")

    def test_get_kingdom(self):
        self.assertEqual(self.my_mammal.get_kingdom(), "animals")
        self.assertEqual(self.my_mammal._Mammal__kingdom, "animals")

    def test_info(self):
        self.assertEqual(self.my_mammal.info(), "Human is of type Human-type")
        self.assertEqual(self.my_mammal.name, "Human")
        self.assertEqual(self.my_mammal.type, "Human-type")

if __name__ == "__main__":
    unittest.main()