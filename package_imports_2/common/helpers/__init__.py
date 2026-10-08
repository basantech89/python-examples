from .calculator import Calc


def say_hello(name: str):
    return f"Hello, {name}!"


def factorial(n: int) -> int:
    return 1 if n == 0 else n * factorial(n - 1)
