int	binary_search(int array[], int item, int len)
{
	int	low;
	int	high;
	int	mid;
	int	current_element;

	low = 0;
	high = len - 1;
	while (low <= high)
	{
		mid = (low + high) / 2;
		current_element = array[mid];
		if (item == current_element)
			return (mid);
		else if (item < current_element)
			high = mid - 1;
		else
			low = mid + 1;
	}
	return (-1);
}
