def fizzbuzz(x: int, y: int, n: int) -> list[str]:
    """
    https://open.kattis.com/problems/fizzbuzz
    """
    result = []
    for i in range(1, n + 1):
        if i % x == 0 and i % y == 0:
            result.append("FizzBuzz")
        elif i % x == 0:
            result.append("Fizz")
        elif i % y == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result
