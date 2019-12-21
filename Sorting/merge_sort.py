def merge_sort(arr):
	if len(arr) == 1:
		return
	else:
		mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]
		merge_sort(L)
		merge_sort(R)
		l,r,i = 0,0,0
		while l < len(L) and r < len(R):
			if L[l] < R[r]:
				arr[i] = L[l]
				l += 1
			else:
				arr[i] = R[r]
				r += 1
			i += 1
		while l < len(L):
			arr[i] = L[l]
			l += 1
			i+=1
		while r < len(R):
			arr[i] = R[r]
			r+= 1
			i+=1
arr = [4, 5, 2, 1, 3]
merge_sort(arr)
print(arr)

