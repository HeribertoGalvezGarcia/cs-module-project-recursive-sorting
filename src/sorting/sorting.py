from typing import Sequence, TypeVar

T = TypeVar('T')


# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arr_a: Sequence[T], arr_b: Sequence[T]) -> Sequence[T]:
    elements = len(arr_a) + len(arr_b)
    merged_arr = [0] * elements

    i = j = k = 0

    while i < len(arr_a) and j < len(arr_b):
        if arr_a[i] < arr_b[j]:
            merged_arr[k] = arr_a[i]
            i += 1
        else:
            merged_arr[k] = arr_b[j]
            j += 1

        k += 1

    while i < len(arr_a):
        merged_arr[k] = arr_a[i]
        i += 1
        k += 1

    while j < len(arr_b):
        merged_arr[k] = arr_b[j]
        j += 1
        k += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr: Sequence[T]) -> Sequence[T]:
    if (arr_len := len(arr)) <= 1:
        return arr

    arr_a = arr[:(mid := arr_len // 2)]
    arr_b = arr[mid:]

    arr_a = merge_sort(arr_a)
    arr_b = merge_sort(arr_b)

    arr = merge(arr_a, arr_b)

    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    ...


def merge_sort_in_place(arr, l, r):
    # Your code here
    ...
