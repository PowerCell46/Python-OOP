from unittest import TestCase, main

from work_file import HashTable


class TestCustomHashTable(TestCase):
    def setUp(self) -> None:
        self.table = HashTable()

    def test_correct_initializing(self):
        self.assertEqual(4, self.table._HashTable__max_capacity)
        self.assertEqual([None] * 4, self.table._HashTable__keys)
        self.assertEqual([None] * 4, self.table._HashTable__values)

    def test__getitem_correct(self):
        self.table['name'] = 'Peter'
        self.assertEqual('Peter', self.table['name'])
        self.assertEqual('Peter', self.table.get('name'))

    def test__getitem_key_raises_key_error(self):
        with self.assertRaises(KeyError) as ke:
            result = self.table['Ivan']
        self.assertEqual("'Invalid key!'", str(ke.exception))

    def test_correct_overwrite_on_key(self):
        self.table['name'] = 'Peter'
        self.table['name'] = 'Ivan'
        self.assertEqual('Ivan', self.table.get('name'))

    def test_resizing_table_when_full(self):
        self.table['name'] = 'Peter'
        self.table['age'] = 20
        self.table['profession'] = 'Programmer'
        self.table['favourite sport'] = 'Fitness'
        self.table['favourite movie'] = 'The Dark Knight'
        self.assertEqual(self.table._HashTable__max_capacity, 8)

    def test_index_hash_correct(self):
        result = self.table._HashTable__calculate_index('name')
        self.assertEqual(1, result)

    def test_collision_and_no_free_space_to_the_end_of_the_array_starts_from_the_beginning(self):
        self.table['name'] = 'Peter'
        self.table['age'] = 20
        self.table['is_pet_owner'] = False
        self.table['is_driver'] = True
        key_index = self.table._HashTable__keys.index('is_driver')
        self.assertEqual(key_index, 0)

    def test_get_on_non_existing_key_without_default_value_returns_none(self):
        self.assertIsNone(self.table.get('something'), None)

    def test_existing_key_with_default_value_returns_default_value(self):
        self.assertEqual('not valid', self.table.get('something', 'not valid'))

    def test_deletion_on_already_created_key(self):
        self.table['name'] = 'Peter'
        self.table.delete('name')
        self.assertEqual([None] * 4, self.table._HashTable__keys)
        self.assertEqual([None] * 4, self.table._HashTable__values)

    def test_deletion_on_non_existent_key(self):
        with self.assertRaises(KeyError) as ke:
            self.table.delete('name')
        self.assertEqual("'Invalid key!'", str(ke.exception))


if __name__ == '__main__':
    main()
