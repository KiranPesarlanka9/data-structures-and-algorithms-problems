#https://www.geeksforgeeks.org/print-all-subarrays-with-0-sum/

def find_sub_arrays(arr):
    print(arr)
    sum_log = {}
    _sum = 0 
    for i in xrange(len(arr)):
        _sum += arr[i]
        if _sum in sum_log:
            print sum_log[_sum]+1, i
        sum_log[_sum] = i 


arr = [1, -2, 5, -4, 1, 9, -2] 
find_sub_arrays(arr)
