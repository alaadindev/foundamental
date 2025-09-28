def max_sum_subarray(arr, width):
    max_sum = 0
    window_sum = sum(arr[:width])
    for i in range(len(arr) - width):
        window_sum = window_sum - arr[i] + arr[i + width]
        max_sum = max(window_sum, max_sum)
    return max(max_sum, window_sum)

print(max_sum_subarray([1,3,2,5,3,2,6,7,4,2,4], 4))

