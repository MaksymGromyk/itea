"""
Написати функцію, яка створить  файл numbers.txt, якщо його не існує.
Запишіть у файл 10 чисел, кожне з нового рядка ( згенерувати модулем random від 1 до 100).
Напишіть функцію, яка зчитує ці числа з файлу і обчислює їх суму, виводить цю суму на екран і, водночас,
записує цю суму у інший файл під назвою sum_numbers.txt
"""
from random import randint


def creator():
    with open('numbers.txt', 'w') as file1:
        for e in range(10):
            file1.write('{}{}'.format(randint(1, 100), '\n'))


def adder():
    with open('numbers.txt', 'r') as file1, \
            open('sum_numbers', 'w') as file2:
        summa = 0
        for line in file1:
            summa += int(line.strip())
        file2.write(str(summa))


if __name__ == '__main__':
    creator()
    adder()
