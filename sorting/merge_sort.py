
def merge_sort(array):
    l = 0
    r = len(array) - 1

    if l < r:
        mid = (l + r) // 2
        left = array[:mid + 1]
        right = array[mid + 1:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        m, n = len(left), len(right)

        while i < m and j < n:
            if left[i] <= right[j]:
                array[k] = left[i]
                i+=1

            else:
                array[k] = right[j]
                j+=1

            k+=1

        while i < m:
            array[k] = left[i]
            i+=1
            k+=1

        while j < n:
            array[k] = right[j]
            j+=1
            k+=1

arr = [5, 1, 1, 2, 0, 0]
merge_sort(arr)
print(arr)




