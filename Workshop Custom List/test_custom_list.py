from unittest import TestCase, main
from figures import CustomList


class TestCustomList(TestCase):
    def setUp(self) -> None:
        self.lst = CustomList()

    def test_append_method(self):
        self.lst.append(1)
        self.assertEqual([1], self.lst._data)

    def test_remove_with_valid_index(self):
        self.lst.append(2)
        result = self.lst.remove(0)
        self.assertEqual(2, result)
        self.assertEqual([], self.lst._data)

    def test_remove_with_empty_list(self):
        with self.assertRaises(IndexError) as err:
            self.lst.remove(2)
        self.assertEqual('pop from empty list', str(err.exception))

    def test_remove_with_invalid_index(self):
        with self.assertRaises(IndexError) as err:
            self.lst.append(1)
            self.lst.remove(10)
        self.assertEqual('pop index out of range', str(err.exception))

    def test_get_with_valid_index(self):
        self.lst.append(10)
        self.assertEqual(10, self.lst.get(0))

    def test_get_with_invalid_index(self):
        with self.assertRaises(IndexError) as err:
            # self.lst.append(1)
            self.lst.get(1)
        self.assertEqual('list index out of range', str(err.exception))

    def test_extend_method(self):
        self.lst.append(1)
        self.assertEqual([1, 2, 3], self.lst.extend([2, 3]))

    def test_insert_method_with_valid_index(self):
        self.lst.append(1)
        self.lst.insert(0, 0)
        self.assertEqual([0, 1], self.lst._data)

    def test_insert_method_with_way_bigger_index(self):
        self.lst.append(1)
        self.lst.insert(10, 10)
        self.assertEqual([1, 10], self.lst._data)

    def test_insert_method_with_way_lesser_index(self):
        self.lst.append(1)
        self.lst.insert(-10, 0)
        self.assertEqual([0, 1], self.lst._data)

    def test_pop_method_with_non_empty_list(self):
        self.lst.append(1)
        res = self.lst.pop()
        self.assertEqual([], self.lst._data)
        self.assertEqual(1, res)

    def test_pop_method_with_empty_list(self):
        with self.assertRaises(IndexError) as err:
            self.lst.pop()
        self.assertEqual('pop from empty list', str(err.exception))

    def test_clear_method(self):
        self.lst.append(1)
        self.lst.extend([2, 3, 4, 5])
        self.lst.clear()
        self.assertEqual([], self.lst._data)

    def test_index_method_with_correct_value(self):
        self.lst.extend([1, 2, 3, 4])
        self.assertEqual(3, self.lst.index(4))

    def test_index_method_with_incorrect_value(self):
        with self.assertRaises(ValueError) as err:
            self.lst.append(1)
            self.lst.index(10)
        self.assertEqual('10 is not in list', str(err.exception))

    def test_count_method_with_one_element_or_more(self):
        self.lst.append(1)
        self.lst.extend([2, 2])
        self.assertEqual(2, self.lst.count(2))
        self.assertEqual(1, self.lst.count(1))

    def test_count_method_with_zero_elements(self):
        self.assertEqual(0, self.lst.count(1))

    def test_reverse_method(self):
        self.lst.extend([el for el in range(5)])
        self.assertEqual([4, 3, 2, 1, 0], self.lst.reverse())
        self.assertEqual([4, 3, 2, 1, 0], self.lst._data)

    def test_copy_method(self):
        self.lst.extend(el for el in range(5))
        copy = self.lst.copy()
        self.assertNotEqual(self.lst, copy)

    def test_size_method(self):
        self.assertEqual(0, self.lst.size())
        self.lst.append(1)
        self.assertEqual(1, self.lst.size())

    def test_add_first_method(self):
        self.lst.add_first(1)
        self.assertEqual([1], self.lst._data)
        self.lst.add_first(0)
        self.assertEqual([0, 1], self.lst._data)

    def test_dictionize_method_with_one_element(self):
        self.lst.append(1)
        self.assertEqual({1: " "}, self.lst.dictionize())

    def test_dictionize_method_with_even_elements(self):
        self.lst.extend([1, 2])
        self.assertEqual({1: 2}, self.lst.dictionize())

    def test_dictionize_method_with_odd_elements(self):
        self.lst.extend([el for el in range(5)])
        self.assertEqual({0: 1, 2: 3, 4: " "}, self.lst.dictionize())

    def test_move_method_with_smaller_than_list_value(self):
        self.lst.extend([el for el in range(5)])
        self.lst.move(2)
        self.assertEqual([2, 3, 4, 0, 1], self.lst._data)

    def test_move_method_with_bigger_than_list_value(self):
        self.lst.extend([el for el in range(10)])
        with self.assertRaises(ValueError) as err:
            self.lst.move(12)
        self.assertEqual('Invalid amount!', str(err.exception))

    def test_sum_with_numbers(self):
        self.lst.extend([el for el in range(3)])
        self.assertEqual(3, self.lst.sum())

    def test_sum_with_mixed_values(self):
        self.lst.extend([el for el in range(3)])
        self.lst.append('Hello')
        self.assertEqual(8, self.lst.sum())

    def test_sum_with_empty_list(self):
        self.assertEqual(0, self.lst.sum())

    def test_overbound_with_numbers(self):
        self.lst.extend([el for el in range(10)])
        self.assertEqual(9, self.lst.overbound())

    def test_overbound_with_mixed_values(self):
        self.lst.extend([el for el in range(10)])
        self.lst.add_first("Some random long sentence...")
        self.assertEqual(0, self.lst.overbound())

    def test_overbound_with_empty_list(self):
        with self.assertRaises(ValueError) as err:
            self.lst.overbound()
        self.assertEqual('No such value in an empty list!', str(err.exception))

    def test_underbound_with_numbers(self):
        self.lst.extend([el for el in range(15)])
        self.assertEqual(0, self.lst.underbound())

    def test_underbound_with_mixed_values(self):
        self.lst.extend([el + 1 for el in range(10)])
        self.lst.append('')
        self.assertEqual(10, self.lst.underbound())

    def test_underbound_with_empty_list(self):
        with self.assertRaises(ValueError) as err:
            self.lst.underbound()
        self.assertEqual('No such value in an empty list!', str(err.exception))


if __name__ == '__main__':
    main()
