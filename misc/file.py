def next_greater(arr):
    """
    Finds the next greater element in the array
    """

    stack = []
    ng = [-1] * len(arr)

    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            ng[stack.pop()] = i

        stack.append(i)

    return ng

arr = [1, 3, 5, 4]
print(next_greater(arr))
