'''
Створіть новий файл у текстовому редакторі і напишіть 3 рядки тексту у ньому про можливості Python.
Кожен рядок повинен починатися з фрази: In Python you can .... Збережіть файл під ім’ям possibilities.txt. Напишіть функцію,
яка зчитує файл і виводить текст з перебором рядків об’єкта файлу і зі збереженням рядків у списку з подальшим виведенням списку поза блоком with
'''


def reader():
    with open('possibilities.txt', 'r') as file1:
        file_lines = [x.strip() for x in file1.readlines()]
        for e in file_lines:
            print(e)


if __name__ == '__main__':
    reader()
