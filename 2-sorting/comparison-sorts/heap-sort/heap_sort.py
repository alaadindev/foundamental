#bubble up, logic wise bubble up is less abstract but slower
def heap_sort_up(arr):
    n = len(arr)-1
    heapfiy_up(arr, n)
    for i in range(n, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapfiy_up(arr, i-1)
    return arr
    
    
def heapfiy_up(arr, n):
    swap = False
    for i in range(n, -1, -1):
        if i == 0: continue
        parent = (i - 1) // 2
        if arr[i] > arr[parent]:
            arr[i], arr[parent] = arr[parent], arr[i]
            swap = True
    if swap:
        return heapfiy_up(arr, n)
    return arr

def heapify(arr, n, i):
    largest = i
    left = 2*i +1
    right = 2*i +2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    
def heap_sort(arr):
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr

print(heap_sort_up([3, 2, 3, 7, 5, 6, 4]))
print(heap_sort([3, 2, 3, 7, 5, 6, 4]))