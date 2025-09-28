def bubble_sort(arr):
    for i in range(len(arr)): #max possible sort loop
        swapped = False #flag for if we swapped any item yet
        for j in range(len(arr)-1 - i): #ignore already sorted items to the most right
            if arr[j] > arr[j+1]: #check if current value is greater then next value
                #swap item in arr
                temp = arr[j+1] 
                arr[j+1] = arr[j]
                arr[j] = temp
                #set swapped flag as True
                swapped = True
        if not swapped: #exit if we didn't swap sorting is finished
            break
    return arr

print(bubble_sort([2,5,1,3,6,7,9,4]))