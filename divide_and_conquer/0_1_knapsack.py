def knapsack(capacity, weights, profits, index):
    if index > len(weights) - 1:
        return 0

    elif weights[index] <= capacity:
        opt1 = profits[index] + knapsack(capacity - weights[index], weights, profits, index + 1)
        opt2 = knapsack(capacity, weights, profits, index + 1)
        return max(opt1, opt2)

    else:
        return 0

weights = [3, 1, 2, 5]
profits = [31, 26, 17, 72]
capacity = 7

print(knapsack(capacity, weights, profits, 0))
