# Sorting Algorithms

## 1.QuickSort 

QuickSort is a divide-and-conquer algorithm that selects a 'pivot' and partitions the array into smaller and larger subarrays. It recursively sorts the subarrays.

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
