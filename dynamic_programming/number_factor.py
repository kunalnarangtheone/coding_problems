def num_factor(n):
    lookup = dict()

    def do_num_factor(n):
        if n in (0, 1, 2):
            return 1

        elif n == 3:
            return 2

        else:
            if n not in lookup:
                lookup[n] = num_factor(n - 1) + num_factor(n - 3) + num_factor(n - 4)

            return lookup[n]

    return do_num_factor(n)


def num_factor_bottom_up(n):
    num_factors = [0 for i in range(n + 1)]
    num_factors[0] = 1
    num_factors[1] = 1
    num_factors[2] = 1
    num_factors[3] = 2

    for i in range(4, n + 1):
        num_factors[i] = num_factors[i - 1] + num_factors[i - 3] + num_factors[i - 4]

    return num_factors[n]

print(num_factor(7))
print(num_factor_bottom_up(7))
