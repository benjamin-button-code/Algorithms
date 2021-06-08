from typing import List


def quick_sort(collection: List, reverse=False) -> List:
	"""A pure Python implementation of quick sort algorithm.
    :param collection: a mutable collection of comparable items
    :return: the same collection ordered by ascending"""
	if len(collection) < 2:
		return collection
	pivot = collection.pop()
	greater: List[int] = []  # All elements from collection which greater pivot
	lesser: List[int] = []  # All elements from collection which less or equal pivot
	for element in collection:
		(greater if element > pivot else lesser).append(element)

	if (not reverse):
		return quick_sort(lesser) + [pivot] + quick_sort(greater)
	else:
		return quick_sort(greater) + [pivot] + quick_sort(lesser)

