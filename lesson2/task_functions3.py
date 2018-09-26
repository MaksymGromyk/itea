"""
Написати функцію, яка випадковим чином вертає число у проміжку від 0 до 100. ( random_100)
Відповідно Написати функцію (summarizer). Яка містить змінну result=0.
Функція summarizer викликає функцію random_100 і додає до суми рузультат.
Якщо результат більше 100 то надрукуйте результат.
"""
from random import randint


def random_100():
    return randint(0, 100)


def summarizer():
    result = 0
    while result < 1000:
        result += random_100()
    return result


if __name__ == '__main__':
    print('The random summ higher than 1000 is {}'.format(summarizer()))
