
from random import randint


def retry(*dec_arcgs, **dec_kwargs):
    def real_wrapper(func):
        def wrapper(*args, **kwargs):
            for x in range(dec_kwargs['efforts']):
                try:
                    return(func())
                except ImportError:
                    pass
            return "No result"
        return wrapper
    return real_wrapper


@retry(efforts=2)
def gen_random():
    randinteger = randint(1, 10)
    print(randinteger)
    if randinteger == 1:
        return randinteger
    else:
        raise ImportError


def run():
    print(gen_random())


if __name__ == '__main__':
    run()
