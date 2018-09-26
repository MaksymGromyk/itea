"""
Написати функцію (len_of_args), яка приймає ключові та позиційні аргументи
(вертає довжину позиційних елементів - len(args) ) . Також  написати функцію rand_of_el,
яка двічі викликає функцію len_of_args  і вертає різницю результатів.
Викликати функцію rand_of_el і надрукувати результат.
"""
from task_functions3 import random_100


def len_of_args(*args, **kwargs):
    return len(str(random_100()))


def rand_of_el():
    action = [len_of_args(random_100()), len_of_args(random_100(), random_100())]
    return action[1] - action[0]


if __name__ == '__main__':
    print('The subtraction of to random lenghts is {}'.format(rand_of_el()))
