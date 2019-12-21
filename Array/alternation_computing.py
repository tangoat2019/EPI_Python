def alternation_computing(arr):
    for i in range(len(arr) -1):
        if i== 0:
            if arr[i] > arr[1]:
                arr[i], arr[1] = arr[1], arr[i]
        if i %2 == 1:
            if i < len(arr)-1 and arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        else:
            if 0 <i < len(arr)-1 and arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

arr = [1,2,3,4,5,6,7,8,9]
alternation_computing(arr)

for i in range(len(arr)):
    print(arr[i])