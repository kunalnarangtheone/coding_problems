def power(num, n):
    """To calculate num^n, example, 2^3 = 8, 2^-1 = 0.5, 2^0 = 1"""
    assert n >= 0 and n == int(n), "Exponent should be positive and integer!"
    if n == 0:
        return 1
    elif n == 1:
        return num
    elif num < 0:
        return 1 / power(abs(num), n)
    else:
        return num * power(num, n - 1)
