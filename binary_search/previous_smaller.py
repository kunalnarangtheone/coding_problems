
def previous_smaller(arr):
    l = 0
    r = len(arr) - 1

    while l < r:
        mid = (l + r + 1) // 2

        if target < arr[mid]:
            r = mid - 1

        else:
            l = mid

    if target < arr[l]:
        return -1
    
    else:
        return arr[l]

li = [1, 2, 3, 5, 7, 9]
target = 5
# print(previous_smaller(li))

import bisect
print(bisect.bisect_left(li, target))