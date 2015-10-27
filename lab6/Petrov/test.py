import unittest
import random
import lab6


class TestSorting(unittest.TestCase):
    def test_trivial(self):
        arr = [1, 333, 22]
        res = lab6.radixsort(arr)
        expected = [1, 22, 333]
        self.assertFalse(not res)  # check res not empty
        self.assertEqual(expected, res)

    def test_empty(self):
        arr = []
        res = lab6.radixsort(arr)
        expected = []
        self.assertEqual(expected, res)

    def test_alot(self):
        arr = [random.randint(0, 10000) for i in range(100000)]
        arr.sort()
        res = lab6.radixsort(arr)
        self.assertFalse(not res)
        self.assertEqual(arr, res)


if __name__ == '__main__':
    unittest.main()
