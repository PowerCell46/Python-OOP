import unittest

class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Peter", 1500, 10)

    def test_properties(self):
        self.assertEqual(self.worker.name, "Peter")
        self.assertEqual(self.worker.salary, 1500)
        self.assertEqual(self.worker.energy, 10)
        self.assertEqual(self.worker.money, 0)

    def test_increase_energy(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 11)

    def test_with_invalid_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as context:
            self.worker.work()
        self.assertEqual(str(context.exception), "Not enough energy.")

        self.worker.energy = -1
        with self.assertRaises(Exception) as context:
            self.worker.work()
        self.assertEqual(str(context.exception), "Not enough energy.")

    def test_work_money(self):
        self.worker.work()
        self.assertEqual(self.worker.money, self.worker.salary)

    def test_work_energy(self):
        self.worker.work()
        self.assertEqual(self.worker.energy, 9)
        
    def test_get_info(self):
        self.assertEqual(self.worker.get_info(), f'Peter has saved 0 money.')

if __name__ == "__main__":
    unittest.main()
