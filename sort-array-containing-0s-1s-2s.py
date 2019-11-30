def sort_array(arr):
    print(arr)
    lo = 0
    hi = len(arr) - 1
    mid = 0
    while mid <= hi:
        if arr[mid] == 0:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            mid += 1
            lo += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] ==2:
            arr[hi], arr[mid] = arr[mid], arr[hi]
            hi -= 1
        print(arr)
    print arr


arr = [0,1,2,2,1,0,1,0,2,1]
sort_array(arr)

