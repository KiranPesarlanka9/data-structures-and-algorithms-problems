def check(arr):

    sum_log = set()
    _sum = 0 

    for i in xrange(len(arr)):
        if _sum in sum_log:
            return True
        _sum += 1
        sum_log.add(_sum)

    return False

arr = [1, 0, -2, 5, -4, 1, 9, -2] 
print(check(arr))
