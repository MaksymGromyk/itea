"""
Напишіть функцію max_of_three, яка приймає три числа і вертає максимальне із них. Викликати функцію і надрукувати результат.
"""


def max_of_three(*args):
    return max(*args)


if __name__ == '__main__':
    print(max_of_three(input('Please type three integers after the dot\n . ')))
