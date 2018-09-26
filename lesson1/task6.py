#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    .Створити список ( students ), що містить lloyd, alice, tyler
    .Для кожного студента надрукувати інформацію у читабельному форматі
    .Напишіть функцію average ( Приймає список, вертає результат.
Всередині функції викличіть вбудовану функцію sum() передавши аргумент.
Результат помістити в змінну total. Привести total до типу float ( число з плаваючою точкою).
Поділити total на кількість елементів у вхідному списку використавши len функцію. Вернути результат.
    .Написати функцію get_letter_grade ( Використати if elif else. Якщо  90 і більше A, 70-90 B, 50-70 C, решта D.
Функція примає число вертає Оцінку A, B, C або D.)
    .перевірити функцію get_letter_grade. Знайти середню оцінку по домашніх завданнях для кожного студента і надрукувати.
(Тобто спочатку викликати функцію average[‘homework’], і передати результат в функцію get_letter_grade)
    .Знайти середню оцінку для всього класу. ( в числовому і буквенному виразі )
"""
lloyd = {"name": "Lloyd", "homework": [90.0, 97.0, 75.0, 92.0], "quizzes": [88.0, 40.0, 94.0], "tests": [75.0, 90.0]}
alice = {"name": "Alice", "homework": [100.0, 92.0, 98.0, 100.0], "quizzes": [82.0, 83.0, 91.0], "tests": [89.0, 97.0]}
tyler = {"name": "Tyler", "homework": [0.0, 87.0, 75.0, 22.0], "quizzes": [0.0, 75.0, 78.0], "tests": [100.0, 100.0]}
students = [lloyd, alice, tyler]
for st in students:
    print(
        'Name of student: {}\nMarks:\nHomework: {}\nQuizzes: {}\nTest: {}\n'.format(st['name'], st['homework'], st['quizzes'], st['tests'])
    )
    print(60 * '_')


def average(list_of_marks):
    total = sum(list_of_marks)
    return total / len(list_of_marks)


def get_letter_grade(mark):
    if mark >= 90:
        return 'A'
    elif mark >= 70:
        return 'B'
    elif mark >= 50:
        return 'C'
    else:
        return 'D'


average_marks = []
for st in students:
    average_marks += [average(st['homework'])]
    print(st['name'], average(st['homework']), get_letter_grade(average(st['homework'])))
print('Class average: {} ({})'.format(round(average(average_marks), 2), get_letter_grade(average(average_marks))))
