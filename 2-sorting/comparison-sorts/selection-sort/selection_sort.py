def selection_sort(arr):
    for i in range(len(arr)): #loop over the arr
        min_index = i #init the min index to i
        for j in range(i+1, len(arr)): # find the min index starting from i+1
            if arr[j] < arr[min_index]:
                min_index = j
        #swap min index above i with the current item i
        temp = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = temp
    
    return arr

print(selection_sort([1,4,2,6,8,5,9,2,4]))