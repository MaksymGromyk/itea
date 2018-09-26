"""
Скопіювати функцію add із попереднього прикладу. Написати декоратор cached.
Cуть декоратора в кешуванні роботи функції add. Тобто треба створити словник де ключами будуть аргументи ( позиційні ),
а значенням буде результат виконання функції add. Відповідно декоратор має перевіряти,
чи є дані в словнику(була вже викликана функція add із такими аргументами)  і вернути результат. \
Програмно перевірити чи дані беруться із кешу чи виконується функція add?
"""

# from functools import lru_cache  ''' instead of @cached'''
cache = dict()


def cached(func):
    def wrapper(*args, **kwargs):
        if args not in cache:
            print('not from cache', args)
            result = func(*args, **kwargs)
            cache[args] = result
        else:
            print('from cache', args)
        return cache[args]
    return wrapper


@cached
def add(*args, **kwargs):
    return sum(args)


if __name__ == '__main__':
    add(1, 5, 10)
    add(1, 5, 10)
    add(1, 5, 10)
