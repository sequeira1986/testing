import unittest
import main


class TestIntegersMethod(unittest.TestCase):
    def test_sum_element(self):
        integer_set = main.OperationsIntegers([9, 1, 4, 7, 5, 6])
        self.assertEqual(integer_set.sum_elements(), 32)

    def test_arithmetic_mean(self):
        integer_set = main.OperationsIntegers([9, 1, 4, 7, 5, 6, 10])
        self.assertEqual(integer_set.arit_mean(), 6)

    def test_maxim_element(self):
        integer_set = main.OperationsIntegers([9, 1, 4, 7, 5, 6])
        self.assertEqual(integer_set.max_element(), 9)

    def test_min_elements(self):
        integer_set = main.OperationsIntegers([4, 2, 1, 3, 5])
        self.assertEqual(integer_set.min_element(), 1)

    def test_empty(self):
        empty_set = main.OperationsIntegers([])
        self.assertIsNone(empty_set.min_element())
        self.assertIsNone(empty_set.max_element())
        self.assertIsNone(empty_set.arit_mean())

    def test_duplicate(self):
        integer_set = main.OperationsIntegers([1, 3, 5, 3, 7, 5, 9, 1])
        self.assertEqual(integer_set.sum_elements(), 25)
        self.assertEqual(integer_set.arit_mean(), 5)
        self.assertEqual(integer_set.max_element(), 9)
        self.assertEqual(integer_set.min_element(), 1)

    def test_negative(self):
        integer_set = main.OperationsIntegers([-1, -3, -5, -3, -7, -5, -9, -1])
        self.assertEqual(integer_set.min_element(), -9)
        self.assertEqual(integer_set.arit_mean(), -5.0)
        self.assertEqual(integer_set.max_element(), -1)
        self.assertEqual(integer_set.max_element(), -1)


if __name__ == '__main__':
    unittest.main()
