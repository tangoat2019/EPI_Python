def dutch_flag_problem(arr, target):
    s, e, l = 0, 0, len(arr)-1
    while e <= l:
        if arr[e] < target:
            arr[e], arr[s] = arr[s], arr[e]
            s += 1
            e += 1
        elif arr[e] == target:
            e += 1
        else:
            arr[e], arr[l] = arr[l], arr[e]
            l -=1 

arr = [1,3,2,1,3,1,1,2,3,1,1,1,2,3,2]
dutch_flag_problem(arr, 2)
print(arr)

