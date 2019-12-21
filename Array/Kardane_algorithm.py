def kardane(arr):
	max_so_far, max_here = 0, 0
	for i in range(len(arr)):
		max_here = max(max_here,0) + arr[i]
		max_so_far = max(max_so_far, max_here)
	return max_so_far

arr = [-2, -3, -4, -1, -2, -1, -5, -3]
print(kardane(arr))
