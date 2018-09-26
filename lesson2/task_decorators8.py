"""
Створити лямбда функцію, що множить число на рандом від 1 до 10. Згенерувати список від 1 до 10.
Застосувити лямда функцію до цього списку, відфільтрувати цей список ( позбутись непарних чисел)
і знайти суму списку.
( Використати map, reduce, filter )
"""
from functools import reduce
from random import randint

# x = lambda x: x * randint(1, 10)


def task8():
    li = range(1, 11)
    li_randomized = map(lambda x: randint(1, 10) * x, li)
    print_for_lists(li_randomized)
    li_filtered = filter(lambda x: not x % 2, li)
    print_for_lists(li_filtered)
    print(sum(li_filtered))
    res = reduce(lambda x, y: x + y, [li_filtered])
    print_for_lists(res)


def print_for_lists(list_to_print):
    print(list_to_print)
    for e in list_to_print:
        print(e)


if __name__ == '__main__':
    task8()
