
def house_robber_dp(prizes):
    lookup = dict()

    def house_robber(index):
        if index > len(prizes) - 1:
            return 0

        else:
            if index not in lookup:
                lookup[index] = max(prizes[index] + house_robber(index + 2), house_robber(index + 1))

            return lookup[index]

    return house_robber(0)


def house_robber_bottom_up(amounts):
    hr = [0 for i in range(len(amounts))]

    hr[len(amounts) - 1] = amounts[len(amounts) - 1]
    hr[len(amounts) - 2] = max(amounts[len(amounts) - 2], hr[len(amounts) - 1])

    for i in range(len(amounts) - 3, -1, -1):
        hr[i] = max(amounts[i] + hr[i + 2], hr[i + 1])

    return hr[0]



amounts = [6, 7, 1, 30, 8, 2, 4]

print(house_robber_dp(amounts))
print(house_robber_bottom_up(amounts))
