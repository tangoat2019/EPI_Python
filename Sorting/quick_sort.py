def partition(arr, l, h):
	pivot, i = arr[h], l-1
	for j in range(l,h):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1], arr[h] = arr[h], arr[i+1]
	return i+1

def quick_sort(arr, l, h):
	if len(arr) == 0:
		return None
	if l < h:
		i_p = partition(arr, l, h)
		quick_sort(arr, l, i_p - 1)
		quick_sort(arr, i_p + 1, h)


arr = [4, 5, 2, 1, 3]
quick_sort(arr, 0, len(arr) - 1)
print(arr)

