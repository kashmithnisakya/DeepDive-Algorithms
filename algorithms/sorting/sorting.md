# Sorting Algorithms

## 1.QuickSort 

QuickSort is a divide-and-conquer algorithm that selects a 'pivot' and partitions the array into smaller and larger subarrays. It recursively sorts the subarrays.

### Time Complexity
- Average: $$O(n \log n)$$
- Worst: $$O(n^2)$$ (when poor pivot choices are made)

### Space Complexity
- Average: $$O(\log n)$$ due to recursion.
- Worst: $$O(n)$$ when the recursion depth is equal to the number of elements.

```
FUNCTION QuickSort(array, low, high)
    IF low < high THEN
        pivotIndex = Partition(array, low, high)
        QuickSort(array, low, pivotIndex - 1)   // Recursively sort the left subarray
        QuickSort(array, pivotIndex + 1, high)  // Recursively sort the right subarray
    END IF
END FUNCTION

FUNCTION Partition(array, low, high)
    pivot = array[high]          // Choose the rightmost element as the pivot
    i = low - 1                 // Pointer for the smaller element

    FOR j FROM low TO high - 1 DO
        IF array[j] <= pivot THEN
            i = i + 1           // Increment index of smaller element
            SWAP array[i] WITH array[j]
        END IF
    END FOR

    SWAP array[i + 1] WITH array[high]  // Place the pivot in the correct position
    RETURN i + 1                        // Return the index of the pivot
END FUNCTION
```

## 2.MergeSort

MergeSort divides the array into two halves, recursively sorts them, and merges the sorted halves back together. Merge sort is devide and conquer algorithm.

### Time Complexity
- Average: $$O(n \log n)$$
- Worst: $$O(n \log n)$$

### Space Complexity
- Average: $$O(n)$$ (requires additional space for merging)
- Worst: $$O(n)$$ (requires additional space for merging)

```
FUNCTION MergeSort(array)
    n = LENGTH(array)
    IF n <= 1 THEN
        RETURN array
    END IF

    middle = n / 2
    left = MergeSort(array[0, middle])    // Recursively sort the left half
    right = MergeSort(array[middle, n])   // Recursively sort the right half

    RETURN Merge(left, right)             // Merge the sorted halves
END FUNCTION

FUNCTION Merge(left, right)
    result = []
    WHILE LENGTH(left) > 0 AND LENGTH(right) > 0 DO
        IF left[0] <= right[0] THEN
            APPEND result, left[0]
            left = left[1, LENGTH(left)]
        ELSE
            APPEND result, right[0]
            right = right[1, LENGTH(right)]
        END IF
    END WHILE

    WHILE LENGTH(left) > 0 DO
        APPEND result, left[0]
        left = left[1, LENGTH(left)]
    END WHILE

    WHILE LENGTH(right) > 0 DO
        APPEND result, right[0]
        right = right[1, LENGTH(right)]
    END WHILE

    RETURN result
END FUNCTION
```

## 3.Selection Sort

Selection sort is an in-place comparison sorting algorithm that divides the input list into two parts: the sublist of items already sorted and the sublist of items remaining to be sorted. It repeatedly selects the minimum element from the unsorted portion and swaps it with the first unsorted element.

### Time Complexity
- Average: $$O(n^2)$$
- Worst: $$O(n^2)$$

### Space Complexity
- Average: $$O(1)$$

```
FUNCTION SelectionSort(array)
    n = LENGTH(array)
    FOR i FROM 0 TO n - 1 DO
        minIndex = i
        FOR j FROM i + 1 TO n DO
            IF array[j] < array[minIndex] THEN
                minIndex = j
            END IF
        END FOR
        SWAP array[i] WITH array[minIndex]
    END FOR
    RETURN array
END FUNCTION
```

