def d2b(n):
    """This function tries to do decimal to binary using addition and returns an integer form as result."""
    assert n >= 0 and n == int(n) , "The number should be a positive integer!"

    if n == 0:
        return ""
    else:
        return f"{n % 2}{d2b(n // 2)}"

def decimal_to_binary(n):
    """This function tries to do decimal to binary using addition and returns an integer form as result."""
    assert n >= 0 and n == int(n) , "The number should be a positive integer!"

    if n == 0:
        return 0
    else:
        return 10 * decimal_to_binary(n // 2) + (n % 2)

print(decimal_to_binary(15))
