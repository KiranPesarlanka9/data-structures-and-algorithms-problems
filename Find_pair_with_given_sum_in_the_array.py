def find_pair(arr, s): 
    seen_nums = set()

    for ind in xrange(len(arr)):
        if s-arr[ind] in seen_nums:
            return arr[ind], s-arr[ind]
        seen_nums.add(arr[ind])


arr = [1,2,1,6,4,0,8]
s = 7 

print(find_pair(arr, s))
