def quicksort(arr: list) -> list:
    """
    Quicksort algorithm implementation.
    :param arr: A list of elements to be sorted.
    :return: A sorted list.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)