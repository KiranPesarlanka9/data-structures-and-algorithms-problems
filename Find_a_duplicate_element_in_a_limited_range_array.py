def find_duplicate(arr):
    seen_elements = set()
    for i in xrange(len(arr)):
        if arr[i] in seen_elements:
            return arr[i], i
        seen_elements.add(arr[i])
    return None

arr = [1,3,2,6,2,6,2,1]
print(find_duplicate(arr))
