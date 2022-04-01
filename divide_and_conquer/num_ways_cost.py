
def num_ways_cost(matrix, i, j, cost):

    if i > len(matrix[0]) - 1 or j > len(matrix) - 1 or cost < 0:
        return 0

    elif i == len(matrix[0]) -1 and j == len(matrix) - 1 and matrix[i][j] == cost:
        return 1

    else:
        op1 = num_ways_cost(matrix, i + 1, j, cost - matrix[i][j])
        op2 = num_ways_cost(matrix, i, j + 1, cost - matrix[i][j])

        return op1 + op2


matrix = [
[4, 7, 1, 6],
[5, 7, 3, 9],
[3, 2, 1, 2],
[7, 1, 6, 3]
]

print(num_ways_cost(matrix, 0, 0, 25))
