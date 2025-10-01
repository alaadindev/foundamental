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

#still different then the standard but shell sort this time
def shell_sort(arr):
    n = len(arr) #get the len
    gap = n//2 #set the gap to half of the arr
    while gap > 0: #keep looping until gap is 1 switch to classical insertion
        for i in range(gap): #loop from 0 to gap with i
            for j in range(i+gap, n, gap): #loop from i+gap to end of arr 1 gap step at a time with j 
                temp = arr[j]
                last_pos = j
                for k in range(j-gap, -1, -gap):
                    if arr[k] > temp:
                        arr[k+gap] = arr[k]
                        last_pos = k
                    else:
                        break
                arr[last_pos] = temp
        gap = gap//2
    return arr

print(shell_sort([3,2,0,1,5,4,8,3,4,6,1,7,4,9]))

#print(odd_shell_sort([3,2,6,1,7,4,9]))