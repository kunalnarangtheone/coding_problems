def find_pairs(arr):
    res = []
    arr.sort()
    n = len(arr)

    def backtrack(idx, path):
        if len(path) == 2:
            res.append(path[:])

        for i in range(idx, n):
            if i > idx and arr[i] == arr[i - 1]:
                continue
                
            path.append(arr[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return res

print(find_pairs([1, 2, 3, 4, 5, 1, 2]))

