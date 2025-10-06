def counting_sort(arr):
    count_range = max(arr) - min(arr)
    count = [0]*(count_range+1)
    print(arr)
    for j in range(len(arr)):
        count[arr[j]] +=1
    acc = 0
    print(count)
    for i in range(count_range):
        acc += count[i]
        count[i] = acc 
    print(count)
    for i in range(count_range, 0, -1):
        count[i] = count[i-1]
    count[0] = 0
    print(count)
    newarr =[0] * len(arr)
    for i in range(len(newarr)):
        newarr[count[arr[i]]] = arr[i]
        count[arr[i]] += 1
    print(count)

    return newarr



print(counting_sort([1,0,3,1,3,1]))