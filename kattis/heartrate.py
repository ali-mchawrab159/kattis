def heartrate(beats: int, seconds: float) -> tuple[float, float, float]:
    """
    https://open.kattis.com/problems/heartrate
    """
    bpm = 60 * beats / seconds
    min_bpm = 60 * (beats - 1) / seconds
    max_bpm = 60 * (beats + 1) / seconds
    return (min_bpm, bpm, max_bpm)
