"""
Удосконалити декоратор із 2 завдання, щоб було можливість передати декоратору ключовий  аргумент наприклад time_caching=60,
і відповідно перевіряти чи дані є давнішими ніж time_caching, якщо давнішими наново виконати функцію add.
"""

from time import time, sleep

cache = dict()


def cached(*dexargs, **dec_kwargs):
    def real_wrapper(func):
        def wrapper(*args, **kwargs):
            if args not in cache or cache[args]['time'] + dec_kwargs['time_caching'] < time():
                print('not from cache', args)
                result = func(*args, **kwargs)
                cache[args] = {'time': time(), 'value': result}
            else:
                print('from cache', args)
            return cache[args]['value']
        return wrapper
    return real_wrapper


@cached(time_caching=5)
def add(*args, **kwargs):
    return sum(args)


if __name__ == '__main__':
    add(1, 5, 10)
    add(1, 5, 10)
    sleep(10)
    add(1, 5, 10)
