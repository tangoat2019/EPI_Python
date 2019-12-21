def delete_from_sorted_arr(arr):
    duplicate_temp = arr[0]
    duplicate_temp_cnt = 0
    for cnt in range(1,len(arr)):
        if (arr[cnt] == duplicate_temp):
            arr[cnt] = 0.25
            duplicate_temp_cnt += 1
        else:
            duplicate_temp = arr[cnt]

    cnt0, i = 0, 0
    while i < len(arr):
        if(arr[cnt0] == 0.25):
            if (arr[i] == 0.25):
                i += 1
            else:
                arr[i], arr[cnt0] =arr[cnt0], arr[i]
                cnt0 += 1
        else:
            cnt0 += 1
            i += 1
    return len(arr) - duplicate_temp_cnt

arr = [2,3,5,5,5,7,11,11,13,13]
print(delete_from_sorted_arr(arr))
for i in range(len(arr)):
    print (arr[i])
