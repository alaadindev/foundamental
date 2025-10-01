#some odd implementation more like modified bubble sort then inseration shell sort
def odd_shell_sort(arr):
    n = len(arr)
    gap = n//2
    while gap > 0:
        for i in range(gap):
            for j in range(i, n-gap, gap):
                if arr[j+gap] < arr[j]:
                    arr[j+gap], arr[j] = arr[j], arr[j+gap]
        gap = gap//2
    return arr

print(odd_shell_sort([3,2,6,1,7,4,9]))