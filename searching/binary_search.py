def bs(arr, left, right, ele) -> Optional[int]:
    if left > right:
        return None

    else:
        mid = (left + right) // 2

        if arr[mid] == ele:
            return mid

        elif ele < arr[mid]:
            return bs(arr, left, mid - 1, ele)

        else:
            return bs(arr, mid + 1, right, ele)

def bs2(arr, left, right, ele) -> int:
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == ele:
            return mid

        elif arr[mid] > ele:
            right = mid - 1

        else:
            left = mid + 1

    return -1

arr = [1, 5, 18, 36, 45, 67, 82, 96]
print(bs(arr, 0, len(arr) - 1, 67))
# print(bs2(arr, 0, len(arr) - 1, 67))
