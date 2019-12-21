def binary_search(arr, s, e, val):
	if arr[(e+s)//2] == val:
		return (e+s)//2
	elif arr[(e+s)//2] > val:
		return binary_search(arr, s, (e+s)//2 - 1, val)
	else:
		return binary_search(arr, (e+s)//2 +1, e, val)
arr = [1,2,3,4,5,6,7,8]
print(binary_search(arr,0,len(arr), 7))
