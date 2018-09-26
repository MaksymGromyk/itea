""" Напишіть декоратор ( функцію logg), яка обертає функції.
Суть декоратора  в тому, що він логує (записує у файл) позиційні і ключова аргументи.
В кінці враппера записати у файл ‘Arguments are written\n’.
Також створити дві функції add & multiply, які підповідно додають, перемножують позиційні аргументи і вертають результат.
Обернути функції add & multiply декоратором logg і викликати їх через if __name__ == “__main__”. Перевірити лог файл чи декоратор спрацював.
"""


def logg(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('logg_result.txt', 'a') as target_file:
            target_file.write('args = {}, kwargs = {}\n'.format(str(args), str(kwargs)))
            target_file.write('arguments are written\n')
        return result
    return wrapper


@logg
def add(*args, **kwargs):
    return sum(args)


@logg
def multiply(*args, **kwargs):
    result = 1
    for x in args:
        result *= x
    return result


if __name__ == '__main__':
    add(1, 5, 10)
    multiply(1, 5, 10)
    with open('logg_result.txt', 'r') as target_file:
        print(target_file.read())
