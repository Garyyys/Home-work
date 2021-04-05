from decimal import Decimal


def bank(add: float, sub: float, total = 0):
        if sub == 0:
            total += add
        else:
            total += add
            total -= sub

        if total < 0:
            total = 0
            return f'SUB can not be more than total'
        return f'ADD: {add} SUB: {sub} (total: {total})'

while True:
    print(bank(float(input()), float(input())))





