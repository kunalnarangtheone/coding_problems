
def knapsack(weights, profits, index, capacity):

    if index > len(weights) - 1:
        return 0

    if weights[index] > capacity:
        return 0

    else:
        opt1 = profits[index] + knapsack(weights, profits, index + 1, capacity - weights[index])
        opt2 = knapsack(weights, profits, index + 1, capacity)

        return max(opt1, opt2)


def knapsack_dp(weights, profits, capacity):
    lookup = dict()

    def knapsack(index, capacity):
        if index > len(weights) - 1:
            return 0

        elif weights[index] <= capacity:
            if index not in lookup:
                lookup[index] = max(profits[index] + knapsack(index + 1, capacity - weights[index]),
                    knapsack(index + 1, capacity))

            return lookup[index]

        else:
            return 0

    return knapsack(0, capacity)

weights = [3, 1, 2, 5]
profits = [31, 26, 17, 72]
capacity = 7

print(knapsack(weights, profits, 0, capacity))

print(knapsack_dp(weights, profits, capacity))
