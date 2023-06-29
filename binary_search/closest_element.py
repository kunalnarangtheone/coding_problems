# arr = [1, 2, 3, 4, 5, 11, 12, 13]
arr2 = [1, 2, 3, 4]

l = 0
r = len(arr2) - 1
target = 5

def binary_search(l, r, arr):
    while l < r:
        mid = (l + r) // 2

        if target == arr[mid]:
            return arr[mid]
        
        dist_mid = abs(arr[mid] - target)
        dist_mid_1 = abs(arr[mid + 1] - target)

        if dist_mid > dist_mid_1:
            l = mid + 1

        else:
            r = mid
    

    return arr[l]

print(binary_search(l, r, arr2))





    

