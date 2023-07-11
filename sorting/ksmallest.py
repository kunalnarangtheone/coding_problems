import random

def ksmallest(arr, k):
    n = len(arr)

    def partition(l, r):
        rand = random.randint(l, r)
        arr[l], arr[rand] = arr[rand], arr[l]
        pivot = l

        while l < r:
            while l < n and arr[l] <= arr[pivot]:
                l+=1

            while r >= 0 and arr[r] > arr[pivot]:
                r-=1

            if l < r:
                arr[l], arr[r] = arr[r], arr[l]

        arr[pivot], arr[r] = arr[r], arr[pivot]
        return r
    
    def quickselect(l, r):
        idx = partition(l, r)

        if idx == k - 1:
            return arr[:k]
        
        elif idx > k - 1:
            return quickselect(l, idx - 1)
        
        else:
            return quickselect(idx + 1, r)
        
    return quickselect(0, len(arr) - 1)

print(ksmallest([3, 2, 1, 5, 6, 4], 2))
