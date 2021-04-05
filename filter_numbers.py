# Напишите функцию для фильтрации последовательности чисел таким образом чтобы фильтр возвращал только числа,
# которые являются: 1) только квадратом, 2) простым числом
# Добавьте аннотации типов в функцию
import typing


def filter(sequence: list, condition: typing.Callable):
    result = []
    for i in sequence:
        if condition(i):
            result.append(i)

    return result


def is_square(item: int):
    for i in range(1, item + 1):
        if i * i == item:
            return True
    return False


def is_prime(item: int):
    for i in range(2, item):
        if item % i == 0:
            return False
    return item > 0


def is_odd(item: int):
    return item % 2 == 1


def is_even(item: int):
    return item % 2 == 0


assert filter(range(25), is_square) == [1, 4, 9, 16]
assert filter(range(25), is_prime) == [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
assert filter(range(25), is_odd) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
assert filter(range(25), is_even) == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
