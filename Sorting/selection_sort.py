def selection_sort(arr):
    for j in range(len(arr)):
        k = j
        for i in range(j, len(arr)):
            if arr[i] <arr[k]:
                k = i
        arr[j], arr[k] = arr[k], arr[j]
                
arr = [2,2,4,2,5,2,1,3,6]
selection_sort(arr)
print(arr)