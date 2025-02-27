def abs(n) -> int:
    """
    Return absolute value of parameter n
    :param n:
    :return: absolute value
    """
    if n < 0:
        return -n
    return n


def fibonacci_recursion(n) -> int:
    """
    Calculate fibonacci number (ver. recursive)
    :param n:
    :return: result value
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursion(n - 2) + fibonacci_recursion(n - 1)


def fibonacci_loop(n) -> int:
    """
    Calculate fibonacci number (ver. iterative)
    :param n:
    :return: result value
    """
    n_list = [0, 1]
    for i in range(n - 1):
        n_list.append(n_list[i] + n_list[i + 1])
    return n_list[n]


def factorial_recursion(n) -> int:
    """
    Calculate factorial using recursion
    :param n:
    :return: factorial value
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursion(n - 1)


def factorial_loop(n) -> int:
    """
    Calculate factorial using loop
    :param n:
    :return: factorial value
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def countdown_loop(n):
    for i in range(n, -1, -1):
        if i == 0:
            print("펑~")
        else:
            print(i)


def countdown_recursion(n):
    if n < 0:
        return
    if n == 0:
        print("펑!")
    else:
        print(n)
    countdown_recursion(n - 1)


if __name__ == "__main__":
    print("Absolute Value:", abs(-99))
    print("Fibonacci (Recursive):", fibonacci_recursion(6))
    print("Fibonacci (Loop):", fibonacci_loop(6))
    print("Factorial (Recursive):", factorial_recursion(5))
    print("Factorial (Loop):", factorial_loop(5))

    n = 5
    print("Countdown (Loop):")
    countdown_loop(n)
    print("Countdown (Recursion):")
    countdown_recursion(n)
