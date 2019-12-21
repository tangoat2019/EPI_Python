def insertion_sort(arr):
    for j in range(len(arr)):
        for i in range(j):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
arr = [2,2,4,2,5,2,1,3]
insertion_sort(arr)
print(arr)