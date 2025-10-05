def counting_sort(arr):
    len = max(arr) - min(arr)
    count = [0]*(len)
    for i in range(arr-1):
        count[i] += 1
    
    return arr



print(counting_sort([2,0,8,3,9,5,8,7,1]))