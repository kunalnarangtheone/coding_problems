def fibonacci(n):
    lookup = dict()

    def dp_fibonacci(n):
        if n == 1:
            return 0

        elif n == 2:
            return 1

        else:
            if n not in lookup:
                lookup[n] = dp_fibonacci(n - 1) + dp_fibonacci(n - 2)

            return lookup[n]

    return dp_fibonacci(n)

print(fibonacci(7))
