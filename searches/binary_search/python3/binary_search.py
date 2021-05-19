from types import List, Optional


def binary_search(sorted_collection: List[int], item: int) -> Optional[int]:
    """Implementation of binary search algorithm in Python.

    Be careful collection must be ascending sorted, otherwise result will be
    unpredictable.

    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item value to search
    :return: index of found item or None if item is not found.

    Examples:
    >>> binary_search([0, 5, 7, 10, 15], 0)
    0
    >>> binary_search([0, 5, 7, 10, 15], 15)
    4
    >>> binary_search([0, 5, 7, 10, 15], 5)
    1
    >>> binary_search([0, 5, 7, 10, 15], 6)

    """
    low = 0
    high = len(sorted_collection) - 1
    while (low <= high):
        mid = (low + high) // 2
        current_item = sorted_collection[mid]
        if (current_item == item):
            return (mid)
        elif (item < current_item):
            high = mid - 1
        else:
            low = mid + 1
    return (None)
