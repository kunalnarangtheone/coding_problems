
def next_greater(arr, target):
    l = 0
    r = len(arr) - 1

    while l < r:
        mid = (l + r) // 2

        if target > arr[mid]:
            l = mid + 1

        else:
            r = mid

    return l

    # if target > arr[l]:
    #     return -1
    
    # else:
    #     return arr[l]


print(next_greater([1, 2, 3, 5, 7, 9], 0))

# import bisect
# print(bisect.bisect_right(li, target))