def counting_sort(arr):
    offset = min(arr)
    count_range = max(arr) - offset
    count = [0]*(count_range+1)
    arrlen = len(arr)
    print(arr)
    for j in range(arrlen):
        count[arr[j]-offset] +=1
    acc = 0
    print(count)
    for i in range(count_range+1):
        acc += count[i]
        count[i] = acc 
    print(count)
    for i in range(count_range, 0, -1):
        count[i] = count[i-1]
    count[0] = 0
    print(count)
    newarr =[0] * arrlen
    for i in range(len(newarr)):
        newarr[count[arr[i]-offset]] = arr[i]
        count[arr[i]-offset] += 1
    print(count)

    return newarr



print(counting_sort([1,2,3,1,3,1]))