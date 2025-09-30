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

print(heap_sort_up([3, 2, 3, 7, 5, 6, 4]))