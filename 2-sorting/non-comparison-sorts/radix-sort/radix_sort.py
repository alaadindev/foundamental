import math

def radix_sort(arr):
    arrlen = len(arr)
    right = 10
    pos = 1
    maxnum = max(arr)
    maxpos = 1 if maxnum == 0 else math.floor(math.log10(maxnum))+1
    extract_digit = lambda x: (x//pos)%right 
    while pos <= 10**maxpos: 
        counts = [0]*10
        axarr = [0]*arrlen
        for i in range(arrlen):
            counts[extract_digit(arr[i])] += 1
        aux = 0
        print(counts)
        for i in range(1, len(counts)):
            counts[i] += counts[i-1]
        print(counts)
        for i in range(9,0,-1):
            counts[i] = counts[i-1] 
        counts[0] = 0
        print(counts)
        for i in range(arrlen):
            axarr[counts[extract_digit(arr[i])]] = arr[i]
            counts[extract_digit(arr[i])] += 1
        print(counts)
        arr = axarr.copy()
        pos *= 10
    return axarr

print(radix_sort([14,23,1,19,0,33,26,43,15]))
