n = 4
k = 2

pths = []

def backtrack(index, path, paths):
    if len(path) == k:
        paths.append([p for p in path])
        return

    for x in range(index, n + 1):
        path.append(x)
        backtrack(x + 1, path, paths)
        path.pop()

    return path

backtrack(1, [], pths)
print(pths)
