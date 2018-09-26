"""
 На вхід програми подається один рядок з цілими числами.
Числа розділені пропусками. Необхідно вивести суму цих чисел.
Наприклад, якщо був введений рядок чисел 2 -1 9 6, то результатом роботи програми буде їх сума 16.
Написати 2 функції( 1 функція приймає інпут від юзера, і передає агрумент 2 функції яка робить обчислення і виводить результат)
"""


def task1():
    def input_user():
        var = input("\nEnter str\n")
        print(var)
        process(var)

    def process(input_from_user):
        list_of_int = [int(x) for x in input_from_user.split()]
        print(sum(list_of_int))

    input_user()


if __name__ == '__main__':
    task1()
