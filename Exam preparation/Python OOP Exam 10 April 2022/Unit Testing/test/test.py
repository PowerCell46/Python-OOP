from project.movie import Movie
from unittest import main, TestCase


class TestMovie(TestCase):
    def test_init(self):
        case = Movie("Peter", 2023, 5)
        self.assertEqual(case.name, "Peter")
        self.assertEqual(case.year, 2023)
        self.assertEqual(case.actors, [])
        self.assertEqual(case.rating, 5)

    def test_name_with_empty_string(self):
        with self.assertRaises(ValueError) as ex:
            case = Movie("", 2023, 5)
        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_year_with_1887(self):
        case = Movie("Peter", 1887, 5)
        self.assertEqual(case.year, 1887)

    def test_year_with_1886(self):
        with self.assertRaises(ValueError) as ex:
            case = Movie("Peter", 1886, 5)
        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_add_actor_with_new_one(self):
        case = Movie("Barbie", 2023, 5)
        case.add_actor("Ivan the Clown")
        self.assertEqual(case.actors, ["Ivan the Clown"])

    def test_add_actor_with_the_same_one(self):
        case = Movie("Barbie", 2023, 5)
        case.add_actor("Ivan the Clown")
        self.assertEqual(case.add_actor("Ivan the Clown"), "Ivan the Clown is already added in the list of actors!")

    def test_greater_than_with_current_greater(self):
        barbie = Movie("Barbie", 2023, 4.5)
        oppenheimer = Movie("Oppenheimer", 2023, 5)
        self.assertEqual(oppenheimer.__gt__(barbie), '"Oppenheimer" is better than "Barbie"')

    def test_greater_than_with_the_other_one_greater(self):
        mission_impossible = ("Mission impossible", 2023, 3)
        across_the_spiderverse = ("Across the Spiderverse", 2023, 4.5)
        self.assertEqual(mission_impossible.__gt__(across_the_spiderverse), True)

    def test_greater_than_with_equal_ratings(self):
        tenet = Movie("Tenet", 2020, 4.5)
        batman_begins = Movie("Batman begins", 2008, 4.5)
        self.assertEqual(batman_begins.__gt__(tenet), '"Tenet" is better than "Batman begins"')

    def test_repr(self):
        batman = Movie("The Batman", 2022, 4.5)
        batman.add_actor("Robert Pattinson")
        batman.add_actor("Zoe Kravitz")
        self.assertEqual(str(batman), f"Name: The Batman\n" \
               f"Year of Release: 2022\n" \
               f"Rating: 4.50\n" \
               f"Cast: Robert Pattinson, Zoe Kravitz")


if __name__ == "__main__":
    main()
