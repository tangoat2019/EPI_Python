def find_next_permutation(arr):
    smaller1, smaller2, j, COUNTING = len(arr) -1, len(arr) -1, len(arr) -1, True
    while j >= 0 and COUNTING== True:
        if arr[j] < arr[smaller2]:
            smaller2 = j
            COUNTING= False
        j -= 1
    if arr[smaller2] < arr[smaller1]:
        for i in range(smaller2, smaller1-1):
            temp = arr[i+1]
            arr[i+1] = arr[i]
        arr[smaller2] = temp
    if arr[smaller2] > arr[smaller1]:
        i = smaller1
        while i > smaller2:
            temp = arr[i-1]
            arr[i-1] = arr[i]
            i -= 1
        arr[smaller1] = temp


arr = [1,0,3,2]
find_next_permutation(arr)
for i in range (len(arr)):
    print(arr[i])