
def next_greater(nums):
    """
    Use a monotonically increasing stack
    """
    n = len(nums)
    stack = []
    ans = [-1] * n

    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            ans[stack.pop()] = nums[i]

        stack.append(i)

    return ans

print(next_greater([5, 7, 1, 4, 3, 2]))