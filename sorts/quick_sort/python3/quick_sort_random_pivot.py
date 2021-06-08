from typing import List
from random import randint


def partition(collection: List, left_index: int, right_index: int):
    pivot = collection[left_index]
    i = left_index + 1

    for j in range(left_index + 1, right_index):
        if collection[j] < pivot:
            collection[i], collection[j] = collection[j], collection[i]
            i += 1
    collection[left_index], collection[i -
                                       1] = collection[i - 1], collection[left_index]
    return i - 1


def quick_sort_random_pivot(collection: List, start: int, length: int) -> List:
    """A Python implementation of quick sort algorithm.
:param collection: a mutable collection of comparable items
:param start: a index in collection which we start
:param length: length of collection"""

    if (length > start):
        pivot = randint(start, length - 1)
        collection[pivot], collection[start] = collection[start], collection[pivot]
        pivot_index = partition(collection, start, length)
        quick_sort_random_pivot(collection, start, pivot_index)
        quick_sort_random_pivot(collection, pivot_index + 1, length)
