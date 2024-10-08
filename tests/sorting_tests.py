import unittest
from algorithms.sorting.quicksort import quicksort
from algorithms.sorting.mergesort import mergesort
from algorithms.sorting.selectionsort import selectionsort

arr = [3, 6, 8, 10, 1, 2, 1]

class TestQuickSort(unittest.TestCase):
    def test_quicksort(self):
        self.assertEqual(quicksort(arr), [1, 1, 2, 3, 6, 8, 10])
        self.assertEqual(quicksort([]), [])
        self.assertEqual(quicksort([1]), [1])
        self.assertEqual(quicksort([1, 2]), [1, 2])
        
class TestMergeSort(unittest.TestCase):
    def test_mergesort(self):
        self.assertEqual(mergesort(arr), [1, 1, 2, 3, 6, 8, 10])
        self.assertEqual(mergesort([]), [])
        self.assertEqual(mergesort([1]), [1])
        self.assertEqual(mergesort([1, 2]), [1, 2])
        
class TestSelectionSort(unittest.TestCase):
    def test_selectionsort(self):
        self.assertEqual(selectionsort(arr), [1, 1, 2, 3, 6, 8, 10])
        self.assertEqual(selectionsort([]), [])
        self.assertEqual(selectionsort([1]), [1])
        self.assertEqual(selectionsort([1, 2]), [1, 2])
               
if __name__ == '__main__':
    unittest.main()