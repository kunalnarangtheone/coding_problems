def gcd(num1, num2):
    """Finds the greatest common divisor of two numbers. Both should be integers according to the definition."""

    assert num1 >= num2, "First number should be >= the second number"
    assert num1 == int(num1) and num2 == int(num2), "Both numbers must be integers!"

    if num2 == 0:
        return num1
    else:
        return gcd(abs(num2), abs(num1) % abs(num2))
