#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
.Напишіть код, який приймає рядок як вхідний і повертає рядок задом наперед.
.Юзер вводить строку. (наприклад  inp = ‘saveChangesInTheEditor’). Вивести на екран скільки слів є цьому інпуті.
(враховувати що нове слово починається із великої літери)
.pangram - строка яка містись усі літери англійської абетки. Перевірити чи введена строка є pangram
.Є строка S, ми можемо перетворити кожну букву окремо на малу або велику, щоб створити іншу строку.
Треба вернути список всіх можливих комбінацій. Наприклад є строка var = ‘it’ результатом буде result_list = [‘IT’, “It”, “iT”, ‘it’].
.(hackerrank) Юзер вводить строку. Перевірити чи ця строка є послідовністю цифр. Тобто
         var = ‘91011’  є послідовністю, треба надрукувати ‘YES’.
         var = ‘10001003’ не є послідовністю, треба надрукувати ‘NO’
.(hackerrank) Юзер вводить пароль. Вивести на екран кількість символів, яких не вистачає щоб цей пароль був “складним”.
 Для того щоб пароль був складним потрібно, щоб пароль складався як мінімум із 6 символів, містив у собі по одному символу із вказаних наборів:
numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
"""

import string
from time import sleep


def from_behind(input_string):
    return input_string[::-1]


def capital_words_in_str(input_string):
    count = 0
    for e in input_string:
        if e.isupper():
            count += 1
    print("there {0} {1} capitalized words in the input string".format('are' if count > 1 else 'is', count))


def pangram(input_string):
    alpha = string.ascii_letters
    for e in input_string:
        if e in alpha:
            alpha = alpha.replace(e, '')
    if len(alpha) == 0:
        print('input string is pangram')
    else:
        print('input string is not pangram')


def possible_combinations(input_string):
    result = []
    for e in input_string:
        result += '{}{}'.format(e.capitalize(), e.lower())
    return result


if __name__ == '__main__':
    input_string = input("please type the string after the dot\ninput:  . ")
    sleep(1)
    print('from behind function: ', from_behind(input_string))
    sleep(2)
    capital_words_in_str(input_string)
    sleep(2)
    pangram(input_string)
    sleep(2)
    print('possible_combinations function', possible_combinations(input_string))
