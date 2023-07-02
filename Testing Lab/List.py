import unittest
# from List.extended_list import IntegerList


class TestIntegerList(unittest.TestCase):
    def setUp(self):
        self.my_list = IntegerList(1, 2, 3, 4, 5, 6)

    def test_the_init_method(self):
        self.assertEqual(self.my_list.get_data(), [1, 2, 3, 4, 5, 6])
        self.assertEqual(self.my_list._IntegerList__data, [1, 2, 3, 4, 5, 6])

    def test_the_init_method_with_other_el_than_numbers(self):
        another_list = IntegerList("1", "r", "something")
        self.assertEqual(another_list.get_data(), [])
        self.assertEqual(another_list._IntegerList__data, [])

    def test_add_with_valid_element(self):
        self.assertEqual(self.my_list.add(7), [1, 2, 3, 4, 5, 6, 7])

    def test_add_with_invalid_element(self):
        with self.assertRaises(ValueError) as ex:
            self.my_list.add("8")
        self.assertEqual(str(ex.exception), "Element is not Integer")

    def test_remove_index_with_valid_index(self):
        self.assertEqual(self.my_list.remove_index(1), 2)

    def test_remove_index_with_invalid_index(self):
        with self.assertRaises(IndexError) as ex:
            self.my_list.remove_index(10)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_insert_with_valid_index(self):
        self.my_list.insert(5, 7)
        self.assertEqual(self.my_list.get_data(), [1, 2, 3, 4, 5, 7, 6])

    def test_insert_with_invalid_index(self):
        with self.assertRaises(IndexError) as ex:
            self.my_list.insert(10, 5)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_insert_with_invalid_data(self):
        with self.assertRaises(ValueError) as ex:
            self.my_list.insert(2, "10")
        self.assertEqual(str(ex.exception), "Element is not Integer")

    def test_get_biggest(self):
        self.assertEqual(self.my_list.get_biggest(), 6)

    def test_biggest_with_equal_numbers(self):
        new_list = IntegerList(1, 1, 1, 1, 1)
        self.assertEqual(new_list.get_biggest(), 1)

    def test_get_index_with_valid_el(self):
        self.assertEqual(self.my_list.get_index(1), 0)

    def test_get_index_with_invalid_el(self):
        with self.assertRaises(ValueError) as ex:
            self.assertEqual(self.my_list.get_index(10), 0)
        self.assertEqual(str(ex.exception), "10 is not in list")


if __name__ == "__main__":
    unittest.main()
