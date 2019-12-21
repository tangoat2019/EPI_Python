def heapify(arr,i, length):
  smallest, left, right = i, 2*i+1, 2*i+2
  if left<length and arr[left] < arr[i]:
    smallest = left
  if right<length and arr[right] < arr[smallest]:
    smallest = right
  if smallest != i:
    arr[i], arr[smallest] = arr[smallest], arr[i]
    heapify(arr,smallest,length)


def build_heap(arr):
  for i in range(len(arr), -1, -1):
    heapify(arr, i, len(arr))


def heap_sort(arr):
  build_heap(arr)
  print(arr)
  for i in range(len(arr)-1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    heapify(arr, 0, i)


arr = [ 2,2,2,2,2,2,1,3]
heap_sort(arr)
print(arr)