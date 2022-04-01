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

# li = [3, 2, 1, 5, 6, 4]
li2 = [10, 4, 5, 8, 6]
print(kthsmallest(li2, 2))
print(li2)
