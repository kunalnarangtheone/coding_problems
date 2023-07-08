
def previous_smaller(nums):
    """
    Use a monotonically decreasing stack
    """
    n = len(nums)
    stack = []
    ans = [-1] * n

    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            stack.pop()

        ans[i] = nums[stack[-1]] if stack else -1
        stack.append(i)

    return ans

print(previous_smaller([5, 7, 1, 4, 3, 2]))