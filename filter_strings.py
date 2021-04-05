# Напишите функцию для фильтрации последовательности строк таким образом чтобы фильтр возвращал только строки,
# которые: 1) имеют указанное количество регистронезависимой буквы в строке, 2) являются только буквенным заголовком
# Добавьте аннотации типов в функцию
import typing


def filter(sequence: list, condition: typing.Callable):
    result = []
    for i in sequence:
        if condition(i):
            result.append(i)

    return result


def has_three_a(item: str):
    return item.count('a') + item.count('A') >= 3


def is_alpha_title(item: str):
    for w in item.split(' '):
        if not w.istitle():
            return False
    return True


strings = [
    'Abrakadabra',
    'Abc Abc B',
    'Abc Abc Abc',
    'Chapter 1: Abrakadabra',
    'abc abc abc',
    'awd',
]

assert filter(strings, has_three_a) == ['Abrakadabra', 'Abc Abc Abc', 'Chapter 1: Abrakadabra', 'abc abc abc', ]
assert filter(strings, is_alpha_title) == ['Abrakadabra', 'Abc Abc B', 'Abc Abc Abc', ]
