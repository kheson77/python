from __future__ import annotations
from typing import Any

class NotIntegerError(Exception):
    """Không phải số nguyên"""

    def __init__(self, value: Any = ..., message: str = None) -> NotIntegerError:
        self.value = value
        self.message = message or f"{value} không phải số nguyên!"


class NegativeError(Exception):
    """Không phải số dương"""
    
    def __init__(self, value: Any = ..., message: str = None) -> NegativeError:
        self.value = value
        self.message = message or f"{value} không phải số nguyên dương!"


def factorial(number):
    if type(number) != int: raise NotIntegerError(number)

    if number < 0: raise NegativeError(number)

    result = 1

    for i in range(number, 1, -1):
        result *= i

    return result


list_ = ["hello", 0, 1, -2, 3]

for value in list_:
    try:
        print(f"{value}! =", factorial(value))
    except (NotIntegerError, NegativeError) as e:
        print(e.message)