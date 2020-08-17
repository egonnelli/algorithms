# Implementation of the Quick Sort Algorithm
# O(nlog(n)) time

def quick_sort(array):
	quick_sort_helper(array, 0, len(array) - 1)
	return array

def quick_sort_helper(array, start_idx, end_idx):
	
	if start_idx >= end_idx:
		return

	pivot_idx = start_idx
	left_idx = start_idx + 1
	right_idx = end_idx

	while right_idx >= left_idx:
		if array[left_idx] > array[pivot_idx] and array[right_idx] < array[pivot_idx]:
			swap(left_idx, right_idx, array)
		if array[left_idx] <= array[pivot_idx]:
			left_idx += 1
		if array[right_idx] >= array[pivot_idx]:
			right_idx -= 1
	swap(pivot_idx, right_idx, array)
	left_subarray_smaller = right_idx - 1 - start_idx < end_idx - (right_idx + 1)
	if left_subarray_smaller:
		quick_sort_helper(array, start_idx, right_idx - 1)
		quick_sort_helper(array, right_idx + 1, end_idx)
	else:
		quick_sort_helper(array, right_idx + 1, end_idx)
		quick_sort_helper(array, start_idx, right_idx - 1)

def swap(i, j, array):
	array[i], array[j] = array[j] , array[i]

"""
import numpy as np

array = np.array([7,6,1,2,4,3,5])
quick_sort(array)

#array([1, 2, 3, 4, 5, 6, 7])

"""