def pot(numbers: list[int]) -> int:
    """
    https://open.kattis.com/problems/pot
    """
    total = 0
    for n in numbers:
        base = n // 10
        power = n % 10
        total += base ** power
    return total
