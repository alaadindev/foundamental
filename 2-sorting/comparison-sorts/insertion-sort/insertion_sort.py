def insertion_sort(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            while arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        
    return arr

print(insertion_sort([1,4,2,6,7,2,7,8,5]))