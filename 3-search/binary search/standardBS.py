def BS(arr, target):
    left =0
    right = len(arr)-1
    while left <= right:
        mid = int((left +right)/2)
        if arr[mid] == target:
            return mid
        if target < arr[mid]:
            right = mid-1
        else:
            left = mid+1
            

    return -1


print(BS([1,2,3,4,5,6,8,10], 4))