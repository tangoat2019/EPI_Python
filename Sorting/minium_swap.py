from copy import deepcopy

def minimum_swap(arr):
    sortedArr = deepcopy(arr)
    sortedArr.sort()
    orders = dict()
    cntSwap = 0
    for i,el in enumerate(sortedArr):
        orders[el] = i
    visited = [False for i in range(len(arr))]

    for i in range(len(arr)):
        el = arr[i]
        if orders.get(el) != i and not visited[i]:
            cntCircleNode = 1
            while not visited[i]:
                visited[i] = True
                i = orders.get(arr[i])
                cntCircleNode += 1
            cntSwap += cntCircleNode -1

    return cntSwap

arr = [1,2,2,4,3,5]
print(minimum_swap(arr))
