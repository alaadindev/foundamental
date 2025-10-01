#some false implementation more like modified bubble sort then inseration shell sort
def false_shell_sort(arr):
    n = len(arr)
    gap = n//2
    while gap > 0:
        for i in range(gap):
            for j in range(i, n-gap, gap):
                if arr[j+gap] < arr[j]:
                    arr[j+gap], arr[j] = arr[j], arr[j+gap]
        gap = gap//2
    return arr

#messy but still shell sort this time
def messy_shell_sort(arr):
    n = len(arr) #get the len
    gap = n//2 #set the gap to half of the arr
    while gap > 0: #keep looping until gap is 1 switch to classical insertion
        for i in range(gap): #squence gap with i starting from 0
            for j in range(i+gap, n, gap): #for each index in the gap sequence jump gap step at a time starting from the next gap (i+gap) until end of arr (n)
                temp = arr[j] # store the current value we want to insert
                last_pos = j # store the last position of current value
                for k in range(j-gap, -1, -gap): # go back gap step at a time until zero starting from left gap distance.
                    if arr[k] > temp: # check if the left value is bigger then out stored value for insertion
                        arr[k+gap] = arr[k] # shift the value to the right when its bigger
                        last_pos = k # update what pos our inset should be at when we finish
                    else:
                        break # exit the loop because our stored value is bigger from left value
                arr[last_pos] = temp # insert our store value
        gap = gap//2 # half our gap again
    return arr


def shell_sort(arr):
    n = len(arr)
    gap = n//2
    while gap > 0:
        for i in range(gap, n):# loop from the end until our first gap squence
            temp = arr[i] # item we want to insert
            j = i
            # shift elements to the right if they are bigger then our temp and we having reach our first gap squence
            while j >= gap and arr[j-gap] > temp:  
                arr[j] = arr[j-gap] # shift left item (j-gap) to the right (j)
                j-= gap # move on to the prevous gap squence
            arr[j] = temp # insert our item to j which index is the last one shifted
        gap = gap//2 #reduce our gap by half
    return arr
print(shell_sort([]))
#print(messy_shell_sort([3,2,0,1,5,4,8,3,4,6,1,7,4,9]))

#print(odd_shell_sort([3,2,6,1,7,4,9]))