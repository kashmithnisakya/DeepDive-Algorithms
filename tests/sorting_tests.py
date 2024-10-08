import unittest
from algorithms.sorting.quicksort import quicksort

class TestSortingAlgorithm(unittest.TestCase):
    def test_quicksort(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        self.assertEqual(quicksort(arr), [1, 1, 2, 3, 6, 8, 10])
        self.assertEqual(quicksort([]), [])
        self.assertEqual(quicksort([1]), [1])
        self.assertEqual(quicksort([1, 2]), [1, 2])
        
if __name__ == '__main__':
    unittest.main()