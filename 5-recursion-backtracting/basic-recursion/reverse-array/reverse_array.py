def reverse_array(arr, start=0, end=None):
    if end == None:
        end = len(arr)-1
    if start >= end:
        return arr
    arr[start], arr[end] = arr[end], arr[start]
    return reverse_array(arr, start+1, end-1)

print(reverse_array([2,1,5,3,7,2,9]))