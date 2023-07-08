
def next_smaller(nums):
    """
    Monotonically decreasing array
    """
    n = len(nums)
    stack = []
    ans = [-1] * n

    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            ans[stack.pop()] = nums[i]

        stack.append(i)

    return ans

print(next_smaller([5, 7, 1, 4, 3, 2]))
