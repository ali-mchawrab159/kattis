def speedlimit(records: list[tuple[int, int]]) -> int:
    """
    https://open.kattis.com/problems/speedlimit
    """
    total_distance = 0
    previous_time = 0

    for speed, time in records:
        hours = time - previous_time
        total_distance += speed * hours
        previous_time = time

    return total_distance
