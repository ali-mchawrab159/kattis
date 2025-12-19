def abc(numbers: list[int], order: str) -> list[int]:
    """
    https://open.kattis.com/problems/abc
    """
    sorted_numbers = sorted(numbers)
    mapping = {
        "A": sorted_numbers[0],
        "B": sorted_numbers[1],
        "C": sorted_numbers[2],
    }
    return [mapping[c] for c in order]
