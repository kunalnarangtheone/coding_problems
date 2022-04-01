def kthsmallest(arr, k):

    def partition(l, r):
        i = l
        pivot = arr[r]

        for j in range(l, r):
            if arr[j] <= arr[r]:
                arr[i], arr[j] = arr[j], arr[i]
                i+=1

        arr[i], arr[r] = arr[r], arr[i]
        return i

    def quickselect(l, r):
        index = partition(l ,r)

        if index == k:
            return arr[index]

        elif index > k:
            return quickselect(l, index - 1)

        else:
            return quickselect(index + 1, r)

    return quickselect(0, len(arr) - 1)

def find_median(arr):
    if len(arr) % 2 != 0:
        return kthsmallest(arr, len(arr) // 2)

    else:
        v1 = kthsmallest(arr, len(arr) // 2)
        v2 = kthsmallest(arr, (len(arr) // 2) - 1)
        return float((v1 + v2) / 2)

print(find_median([4, 3, 4, 7]))
