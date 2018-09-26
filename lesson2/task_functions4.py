"""
Написати функцію ( find_super ). Функція приймає на вхід число.
А повинна вернути суму цифр вхідного числа ( якщо ця сума менша 10).
Тобто якщо вхідне число = 12345. То сума цифр = 15 ( 15 > 10 ),
тобто треба вернути суму цифр  вже 15. (застосувати рекурсію)
"""


def find_super(integer):
    string = str(integer)
    result = 0
    for e in string:
        result += int(e)
    return result


if __name__ == '__main__':
    integer = input('Please type after the dot the integer which you want me to count\n. ')
    print('The amount of digits of the input number is {}'.format(find_super(integer)))
