#Bubblesort algorithm in python
#Time complexity - O(N^2)

def bubble_sort(array):
	"""
	This functions implements the bubble sort algorithm
	"""
	is_sorted = False
	counter = 0
	while not is_sorted
		is_sorted = True
		for i in range(len(array) - 1 - counter)
			if array[i] > array[i+1]:
				swap(i, i+1, array)
				is_sorted = False
		counter += 1
	return array


def swap(i,j,array):
