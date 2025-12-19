def oddities(numbers: list[int]) -> list[str]:
    """
    https://open.kattis.com/problems/oddities
    """
    return ["even" if x % 2 == 0 else "odd" for x in numbers]
