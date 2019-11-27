#i/p: 1,0,1,0,1,0,0,0,0,1
#0/p: 0,0,0,0,0,0,1,1,1,1

def sort_arr(arr):
    j = 0 
    for i in xrange(len(arr)):
        if arr[i]==0:
            arr[j] = arr[i]
            j += 1
    for k in xrange(j, len(arr)):
        arr[k] = 1 
    return arr 

arr = [1,0,1,0,1,0,0,0,0,1]
print(sort_arr(arr))
