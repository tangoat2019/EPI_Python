def increase_integer(arr):
    dot = 0
    move_over= True
    for cnt in range(len(arr)):
        if arr[cnt] < 0:
            dot = cnt
    cnt2 = len(arr) - dot +1
    while move_over:
        if arr[cnt2] == 9:
            arr[cnt2] = 0
            if cnt2 == 0:
                add_one_to_front(arr)
                move_over = False
            cnt2 -= 1
        else:
            arr[cnt2] += 1
            move_over = False


def add_one_to_front(arr):
    k = len(arr)
    arr.extend([0])
    for i in range(k):
        arr[i] = arr[i-1]
        print(arr[i])
    arr[0] = 1


arr = [9,9,9,9,9,-1,0,9]
increase_integer(arr)
#for i in range(len(arr)):
    #print arr[i]