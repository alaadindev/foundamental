import random 
big_random_arr = [random.randint(0, 1000) for _ in range(0, 1000)]
"""
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1): # loop over index from above left until right
        value = arr[i] #get the current value of i index to be inserted
        j = i - 1 # assign j to less then i by 1
        while j >= left and arr[j] > value: #loop if index j bigger/equal to left and value of j (arr[j]) greater then our value
            arr[j + 1] = arr[j] # shift the current value to the right
            j -= 1 # reduce j by 1
        arr[j + 1] = value # j have the last index where the insertion need to go
    print("insertion")

def merge(arr, left, mid, right):
    left_part = arr[left:mid + 1] # get subarr from left to mid(including)
    right_part = arr[mid + 1:right + 1] # get subarr from mid(exluding) to right (including)

    i = j = 0 
    k = left #k is left

    while i < len(left_part) and j < len(right_part): # loop if i less then left subarr and j is less then right subarr
        if left_part[i] <= right_part[j]: # check if current(i) left value less/equal to current(j) right value
            arr[k] = left_part[i] #assign current left value of subarr to our original arr left side
            i += 1 # move current left 1 to the right
        else:
            arr[k] = right_part[j] # assign current right value subarr to the left side of original arr
            j += 1 #move current right 1 to the right
        k += 1 # move index of our original arr to the right by 1

    while i < len(left_part): # loop if index is less then len of our left subarr
        arr[k] = left_part[i] # assign current left value subarr to the original arr from the left side k
        i += 1 # increase our left subarr current index
        k += 1 # increase our original current arr index

    while j < len(right_part): # loop if index is less then len of our right sub arr
        arr[k] = right_part[j] # assign current right value subarr to the original arr from the left side k
        j += 1 # increase our right subarr current index
        k += 1 # increase our original current arr index
    print("merge")

def calc_min_run(n):
    run = 0
    while n >= 64: #loop if n still greater then 64
        if n%2 == 1: #assign run to 1 if length n is odd | remember if we dropped a 1 from right side
            run = 1
        n >>= 1 # throw away one bit from the right(divide by 2)
    return n + run # return min length divisible by 2 + leftover odd number


def tim_sort(arr):
    n = len(arr)
    min_run = calc_min_run(n) # get min length between 32/64

    # Step 1: Sort small runs using insertion sort
    for start in range(0, n, min_run): # loop from 0 to len of arr with min_run step at a time
        end = min(start + min_run - 1, n - 1) #get the min between start index plus our step size and last index of arr, make sure we don't go out of bound
        insertion_sort(arr, start, end) # use insertion sort

    # Step 2: Merge runs in powers of two
    size = min_run # set our size to size of our run
    while size < n: #loop if size still below length of our arr
        for left in range(0, n, 2 * size): # loop from 0 index until length taking double size as step each time
            mid = min(n - 1, left + size - 1) # get the min between last index of arr and left+size -1
            right = min((left + 2 * size - 1), n - 1) # get min between left plus double size -1 and last index of our array

            if mid < right: # if mid smaller then right merge them
                merge(arr, left, mid, right) 

        size *= 2 # double our size each time
    return arr
"""
def insertion_sort(arr, left, right):
    for i in range(left+1, right+1):
        insert_value = arr[i]
        j=i-1
        while j >= left and arr[j] > insert_value:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = insert_value
    return arr

def merge(arr, left, mid, right):
    left_arr = arr[left: mid+1]
    right_arr = arr[mid+1: right+1]
    i=j=0
    k=left
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i+=1
        else:
            arr[k] = right_arr[j]
            j+=1
        k+=1
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i+=1
        k+=1
    while j< len(right_arr):
        arr[k] = right_arr[j]
        j+=1
        k+=1
    return arr

def min_run(n):
    run = 0
    while n >= 64:
        if n % 2 == 1:
            run = 1
        n >>= 1
    return n + run

def tim_sort(arr):
    n = len(arr)
    run = min_run(n)

    for i in range(0, n, run):
        insertion_sort(arr, i, min(i + run-1, n-1) )
    size = run
    while size < n:
        for left in range(0, n, 2*size):
            mid = min(left + size -1, n-1)
            right = min(mid + size, n-1)
            if mid < right:
                merge(arr, left, mid, right)
        size *=2
    return arr


#print(insertion_sort([1,4,2,0,4,7,3,9], 1, 8))
#print(merge([1,3,5,2,4,6], 0, 2, 5))
#print(tim_sort([4, 1, 7, 3, 0, 2, 9, 5]))
print(tim_sort(big_random_arr))