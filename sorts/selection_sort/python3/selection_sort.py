def selection_sort(collection):
    """Implementation of the selection sort algorithm in Python
    
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> selection_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> selection_sort([])
    []
    >>> selection_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    length = len(collection)
    for i in range(length - 1):
        least = i
        for j in range(i + 1, length):
            if (collection[j] < collection[least]):
                least = j
        if (least != i):
            collection[least], collection[i] = collection[i], collection[least]
    return (collection)
