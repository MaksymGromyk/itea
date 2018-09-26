"""
Написати функцію, яка генерує ( рандомно) список списків( 5 вкладених списків ) довжиною 5 елементів.
Відсортувати 1 список по 4 елементу вкладених списків. Вивести відсортований список на екран.
"""
from random import sample


def listogenerator():
    list_of_lists = []
    for e in range(5):
        list_of_lists.append(sample(range(1000), 5) * 5)
    return sorted(list_of_lists, key=lambda list_of_lists: list_of_lists[4])


if __name__ == '__main__':
    print(listogenerator())
