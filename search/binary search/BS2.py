def BS(arr, target):
    left = 0
    right = len(arr)-1
    while (left <= right):
        mid = int((left + right)/2)
        if (target == arr[mid]):
            return mid
        if (target > arr[mid]):
            left = mid
        else:
            right = mid
    return -1

print(BS([1,2,3,4,5,6],4))