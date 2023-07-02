import unittest
from project.hero import Hero
# zoo.hero.

class TestHero(unittest.TestCase):
    def setUp(self):
        self.my_hero = Hero("PowerCell46", 50, 20, 70)

    def testing_the_init(self):
        self.assertEqual(self.my_hero.health, 20)
        self.assertEqual(self.my_hero.username, "PowerCell46")
        self.assertEqual(self.my_hero.level, 50)
        self.assertEqual(self.my_hero.damage, 70)

    def testing_battle_with_invalid_username(self):
        with self.assertRaises(Exception) as ex:
            self.my_hero.battle(self.my_hero)
        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def testing_with_negative_health_and_zero_health(self):
        self.my_hero.health = 0
        enemy = Hero("DarthIvanBG", 41, 50, 40)
        with self.assertRaises(Exception) as ex:
            self.my_hero.battle(enemy)
        self.assertEqual(str(ex.exception), "Your health is lower than or equal to 0. You need to rest")

        self.my_hero.health = -1
        with self.assertRaises(Exception) as ex:
            self.my_hero.battle(enemy)
        self.assertEqual(str(ex.exception), "Your health is lower than or equal to 0. You need to rest")

    def testing_with_invalid_enemy(self):
        enemy = Hero("DarthIvanBG", 41, 0, 40)
        with self.assertRaises(ValueError) as ex:
            self.my_hero.battle(enemy)
        self.assertEqual((str(ex.exception)), f"You cannot fight DarthIvanBG. He needs to rest")

        enemy.health = -1
        with self.assertRaises(ValueError) as ex:
            self.my_hero.battle(enemy)
        self.assertEqual((str(ex.exception)), f"You cannot fight DarthIvanBG. He needs to rest")

    def testing_battle_with_enemy_losing(self):
        enemy = Hero("DarthIvanBG", 1, 100, 10)
        self.assertEqual(self.my_hero.battle(enemy), "You win")
        self.assertEqual(self.my_hero.health, 15)
        self.assertEqual(self.my_hero.level, 51)
        self.assertEqual(self.my_hero.damage, 75)
        self.assertEqual(enemy.health, -3400)

    def testing_battle_with_draw(self):
        enemy = Hero("Kristiyan8", 48, 100, 30)
        self.assertEqual(self.my_hero.battle(enemy), "Draw")
        self.assertEqual(self.my_hero.health, -1420)
        self.assertEqual(enemy.health, -3400)

    def testing_battle_with_a_lose(self):
        enemy = Hero("Ninja", 100, 10_000, 100)
        self.assertEqual(self.my_hero.battle(enemy), "You lose")
        self.assertEqual(self.my_hero.health, -9980)
        self.assertEqual(enemy.level, 101)
        self.assertEqual(enemy.health, 6505)
        self.assertEqual(enemy.damage, 105)

    def testing_the_str_method(self):
        self.assertEqual(self.my_hero.__str__(), f"Hero PowerCell46: 50 lvl\n" \
               f"Health: 20\n" \
               f"Damage: 70\n")


if __name__ == "__main__":
    unittest.main()