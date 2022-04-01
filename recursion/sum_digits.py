import math

def sum_digits(num):
    assert num == int(num), "Number can only be a positive integer!"
    assert num >= 0, "Number cannot be negative!"
    if num == 0:
        return 0
    else:
        return (num % 10) + sum_digits(math.floor(num / 10))
