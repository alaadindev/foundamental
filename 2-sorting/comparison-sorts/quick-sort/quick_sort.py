def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = len(arr)-1
    i=-1
    j=0
    while j < pivot:
        if arr[j] > arr[pivot]:
            j= j+1
        else:
            i=i+1
            arr[i], arr[j] = arr[j], arr[i]
            j=j+1
    i=i+1
    arr[i], arr[pivot] = arr[pivot], arr[i]
    return quick_sort(arr[:i])+ [arr[i]]+ quick_sort(arr[i+1:])

print(quick_sort([2,4,1,5,6,3,7,9,5]))