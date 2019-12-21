def can_reach_end_bforce(arr):
    traverse_stack = []
    traverse_stack.append(arr[0])
    found_it = False

    if arr[0] >= len(arr):
        return true

    for i in range(arr[0]):
        if arr[i] > 0:
            traverse_stack.append(i)

    traverse_stack= traverse_stack[::-1]
    current_index = traverse_stack.pop()

    while len(traverse_stack) > 0 and found_it == False:
        for i in range(current_index):
            if arr[i] > 0 and i not in traverse_stack and (i + current_index) < len(arr):
                traverse_stack.append(i)
            if (i + current_index) == len(arr):
                found_it == True

    return found_it


def can_reach_end(A):
    furthest_reach_so_far, last_index = 0, len(A) - 1
    i=0
    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, A[i] + i)
        i+=1
    return furthest_reach_so_far >= last_index

arr = [6,0,3,0,2,0,0,3,1,7,4,2,0,0,0,0,1,2]
print(can_reach_end(arr))