arr = [3, 5, 7, 11]
n = len(arr)

def combinations():
    res = []
    def backtrack(index, prod, path):
        nonlocal res
        if prod and prod not in res:
            res.append(int(prod))

        for i in range(index, n):
            if arr[i] not in path:
                prod*=arr[i]
                path.append(arr[i])
                backtrack(index + 1, prod, path)
                prod/=arr[i]
                path.pop()

    backtrack(0, 1, [])
    return res

print(combinations())
