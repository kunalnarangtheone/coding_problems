
def previous_greater(nums):
    """
    Use a monotonically increasing stack
    """
    n = len(nums)
    stack = []
    ans = [-1] * n

    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            stack.pop()

        ans[i] = nums[stack[-1]] if stack else -1
        stack.append(i)

    return ans

print(previous_greater([5, 7, 1, 4, 3, 2]))