def find_pairs(arr):
    res = []

    def backtrack(index, path):
        nonlocal res

        if len(path) == 2 and sorted(path[:]) not in res:
            res.append(sorted(path[:]))
            return

        for i in range(index, len(arr)):
            if arr[i] not in path:
                path.append(arr[i])
                backtrack(index + 1, path)
                path.pop()

    backtrack(0, [])
    return res

print(find_pairs([1, 2, 3, 4, 5, 1, 2]))
