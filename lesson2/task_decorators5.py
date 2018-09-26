"""
 Напишіть функцію, яка генерує словник.
 Де ключами є слова square, cubic, four, five. А значення будуть лямбда функції які приймають число як аргумент,
 а вертають піднесення до відповідного степеня.
 У функції по черзі викликати лямбда функції із випадково згенерованим числом від 10 до 20.
"""
from random import randint


def power():
    keys = ['square', 'cubic', 'four', 'five']
    dic = dict(zip(keys, range(2, 6)))
    for e, n in dic.items():
        dic[e] = lambda x: x ** n
        dic[e](randint(10, 20))
    return dic


if __name__ == '__main__':
    power()
