amounts = [6, 7, 1, 30, 8, 2, 4]


def house_robber_amount(amounts, curHouse):
    if curHouse > len(amounts) - 1:
        return 0

    else:
        opt1 = amounts[curHouse] + house_robber_amount(amounts, curHouse + 2)
        opt2 = house_robber_amount(amounts, curHouse + 1)
        return max(opt1, opt2)

print(house_robber_amount(amounts, 0))
