from typing import Sequence, TypeVar

T = TypeVar('T')


# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr: Sequence[T], target: T, start: int = None, end: int = None) -> int:
    if not arr:
        return -1

    start = start if start is not None else 0
    end = end if end is not None else len(arr) - 1

    middle = (start + end) // 2

    if (middle_element := arr[middle]) == target:
        return middle

    if end < start:
        return -1

    if middle_element < target:
        start = middle + 1
    else:
        end = middle - 1

    return binary_search(arr, target, start, end)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively


def agnostic_binary_search(arr: Sequence[T], target: T, start: int = None, end: int = None) -> int:
    if not arr:
        return -1

    ascending = arr[-1] > arr[0]

    if ascending:
        return binary_search(arr, target, start, end)

    start = start if start is not None else 0
    end = end if end is not None else len(arr) - 1

    middle = (start + end) // 2

    if (middle_element := arr[middle]) == target:
        return middle

    if end < start:
        return -1

    if middle_element > target:
        start = middle + 1
    else:
        end = middle - 1

    return agnostic_binary_search(arr, target, start, end)
