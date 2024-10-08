def merge(left: list, right: list) -> list:
    """
    Merge two sorted lists into one sorted list.
    :param left: A sorted list.
    :param right: Another sorted list.
    :return: A merged and sorted list.
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def mergesort(arr: list) -> list:
    """
    Mergesort algorithm implementation.
    :param arr: A list of elements to be sorted.
    :return: A sorted list.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)
    
