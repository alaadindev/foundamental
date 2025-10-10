def bucket_sort(arr):
    normalized = lambda num: num/(max(arr)+1)
    bucketN = lambda num: int(6*normalized(num))
    arrlen = len(arr)
    axarr = [[] for _ in range(6)] 
    for i in range(arrlen):
        axarr[bucketN(arr[i])].append(arr[i])
    for i in range(len(axarr)):
        insertion_sort(axarr[i])
    flat = []
    for subarr in axarr:
        flat.extend(subarr)
    return flat

def insertion_sort(arr):
    for i in range(1,len(arr)):
        j=i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr


print(bucket_sort([2,21,5,100,4,50]))