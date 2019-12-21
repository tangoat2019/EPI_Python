def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(1,len(arr)):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    
arr = [2,2,4,2,5,2,1,3]
bubble_sort(arr)
print(arr)