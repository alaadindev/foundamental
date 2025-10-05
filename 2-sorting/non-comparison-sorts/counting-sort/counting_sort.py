def counting_sort(arr):
    len = max(arr) - min(arr)
    count = [0]*(len)
    for i in range(len(arr)-1):
        count[i] += 1
    acc = 0
    for i in range(len(count)-1):
        acc += count[i]
        count[i] = acc 
    for i in range(count-1, 0, -1):
        count[i] = count[i-1]
    count[0] = 0
    print(count)
    
    return arr



print(counting_sort([2,0,8,3,9,5,8,7,1]))