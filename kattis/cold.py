def cold(temperatures: list[int]) -> int:
    """
    https://open.kattis.com/problems/cold
    """
    return sum(1 for t in temperatures if t < 0)
