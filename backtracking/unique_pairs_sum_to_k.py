def find_all_numbers(nums, k):
    res = []
    def backtrack(index, path):
        nonlocal res
        if len(path) == 2 and sum(path) == k:
            res.append(path[:])
            return

        for i in range(index, len(nums)):
            if nums[i] not in path:
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

    backtrack(0, [])
    return res

print(find_all_numbers([1, 2, 3, 4, 5, 7], 5))
