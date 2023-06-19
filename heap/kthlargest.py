from heapq import heappush, heappop

def kthsmallest(nums, k):
    assert len(nums) > 0, "nums array should exist!"
    assert k > 0, "k should be a positive integer!"
    assert k <= len(nums), "k should be smaller than or equal to the length of the array!"

    heap = []
    
    for num in nums:
        if len(heap) < k:
            heappush(heap, -num)
            continue

        if -num > heap[0]:
            heappop(heap)
            heappush(heap, -num)

    return -heap[0]


print(kthsmallest([1, 5, 2, 9, 4, 3], 3))