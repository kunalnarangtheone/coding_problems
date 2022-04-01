def min_cost(matrix, i, j, end = (4, 4)):

    if i > len(matrix[0]) - 1 or j > len(matrix) - 1:
        return 1000000000

    if i == end[0] and j == end[1]:
        return matrix[i][j]

    opt1 = matrix[i][j] + min_cost(matrix, i + 1, j)
    opt2 = matrix[i][j] + min_cost(matrix, i, j + 1)

    return min(opt1, opt2)

matrix = [
[4, 7, 8, 6, 4],
[6, 7, 3, 9, 2],
[3, 8, 1, 2, 4],
[7, 1, 7, 3, 7],
[2, 9, 8, 9, 3]
]

print(min_cost(matrix, 0, 0))
