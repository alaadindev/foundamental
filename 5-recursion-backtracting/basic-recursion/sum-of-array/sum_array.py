def sum_array(arr, index=0):
    if index == len(arr):
        return 0
    return arr[index]+ sum_array(arr, index+1)

print(sum_array([2,1,5,3,8]))