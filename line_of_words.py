# Дана строка целых чисел `numbers`, разделенных запятой.
# Превратите строку в словарь `result`, где ключ словаря - число в строке, значение - число в кубе.
# По возможности сделайте несколько вариантов решений, используя:
# - цикл for (опционально while)
# - словарное выражение (dict comprehension)
numbers = '1,100,15,17,3,221,9,5,7,2,8,11'
l = len(numbers)
integ = []
i = 0
while i < l:
    s_int = ''
    a = numbers[i]
    while '0' <= a <= '9':
        s_int += a
        i += 1
        if i < l:
            a = numbers[i]
        else:
            break
    i += 1
    if s_int != '':
        integ.append(int(s_int))

numbers = integ
result = {
    number: number ** 2  # key: value
    for number in numbers
}

print(result)


# Ваше решение

# Тесты
# assert all(number in result and result[number] == number * number * number for number in (1, 100, 15, 17, 3, 221, 9, 5, 7, 2, 8, 11))