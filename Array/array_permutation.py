def array_permutation(arr, per):
    for i in range (len(arr)-1):
        print('here')
        current_i_per = i
        if current_i_per != per[current_i_per]:
            while current_i_per != per[current_i_per]:
                i_array_to_change = per[current_i_per]
                current_val_at_i_arr = arr[i_array_to_change]
                arr[i_array_to_change] = arr[current_i_per]
                t = current_i_per
                current_i_per = per[current_i_per]
                per[t] = t
                print('heres')


arr = ['a','b','c','d','e','f','g']
per = [2,0,1,3,5,4,6]
array_permutation(arr, per)

for i in range(len(arr)):
    print(arr[i])
