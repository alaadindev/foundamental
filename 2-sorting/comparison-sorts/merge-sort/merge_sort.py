def merge_sort(arr, ):
    if len(arr) < 2:
        return arr
    mid= len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    return merge(merge_sort(left_arr), merge_sort(right_arr))

def merge(left, right):
    result = []
    i=j=0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
print(merge_sort([5,3,1,5,2,7,6,8,9]))