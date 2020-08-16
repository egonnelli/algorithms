#Bubblesort algorithm in python
#Time complexity - O(N^2)

def bubble_sort(array):
	"""
	This functions implements the bubble sort algorithm
	"""
	is_sorted = False
	counter = 0
	while not is_sorted:
		is_sorted = True
		for i in range(len(array) - 1 - counter)
			if array[i] > array[i+1]:
				swap(i, i+1, array)
				is_sorted = False
		counter += 1
	return array


def swap(i,j,array):
	array[i] , array[j] = array[j], array[i]

"""
import numpy as np

array = np.array([4,5,6,7,1,2,3])
bubble_sort(array)

#array([1, 2, 3, 4, 5, 6, 7])

"""