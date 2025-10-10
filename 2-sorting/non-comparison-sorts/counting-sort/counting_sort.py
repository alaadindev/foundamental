def counting_sort(arr):
    offset = min(arr)
    count_range = max(arr) - offset
    count = [0]*(count_range+1)
    arrlen = len(arr)
    #loop and count each number encounter
    for j in range(arrlen):
        count[arr[j]-offset] +=1
    #acc the count of each num
    acc = 0
    for i in range(count_range+1):
        acc += count[i]
        count[i] = acc 
    #shift the values to the right add zero at index 0
    for i in range(count_range, 0, -1):
        count[i] = count[i-1]
    count[0] = 0
    newarr =[0] * arrlen
    #loop assign each index i value of our old arr
    #to our newarr in index of the value of count index of our old arr
    #of current index minus the offset min
    #increase out count of the value of our index in old arr minus the offset
    #basically next time we encounter a value in old arr we look to our count
    #which store all numbers sorted location and the frequence
    #like count 0, 1, 2, 3
    #           0, 0, 1, 3
    #which mean 0 is at 0 1 is it 0 so 0 doesn't exist, 2 is at 1, 3 at 2 and 3 hence we need to increase it
    for i in range(len(newarr)):
        newarr[count[arr[i]-offset]] = arr[i]
        count[arr[i]-offset] += 1

    return newarr

print(counting_sort([1,2,3,1,3,1]))
