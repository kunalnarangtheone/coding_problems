def partition(arr, l, r):
    pivot = arr[l] # Initialize pivot item
    i, j = l, r # Initialize i and j pointers for traversal

    while i < j: # Do this while i < j

        while i < r and arr[i] <= pivot: # Do this while i < r and the element at ith index is smaller than or equal to pivot. If we find anything that is greater than pivot, stop.
            i+=1

        while arr[j] > pivot: # Decrement j until we find an element that is less than or equal to pivot, at which point, we stop.
            j-=1

        if i < j: # Check if i is still less than j, then just swap them
            arr[i], arr[j] = arr[j], arr[i]

    arr[l], arr[j] = arr[j], arr[l] # Also, swap the element at l and the element at j
    return j # Finally return this found j

def quicksort(arr, l, r):
    if l < r:
        idx = partition(arr, l, r) # Call the partition and find the partioning index
        quicksort(arr, l, idx) # Recursively call quicksort on lower half
        quicksort(arr, idx + 1, r) # Recursively call quicksort on upper half

    return arr

print(quicksort([10, 15, 67, 32, 1, 34, 26, 13], 0, 7))
print(quicksort([10, 3], 0, 1))
