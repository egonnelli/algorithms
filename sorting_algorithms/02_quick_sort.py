#Implementation of the Quick Sort Algorithm

def quick_sort(array):

def quick_sort_helper(array, start_idx, end_idx):
	
	if start_idx >= end_idx:
		return

	pivot_idx = start_idx
	left_idx = start_idx + 1
	right_idx = end_idx

	while right_idx >= left_idx:
		if array[left_idx] > array[pivot_idx] and array[right_idx] < array[pivot_idx]:
			swap(left_idx, right_idx, array)

