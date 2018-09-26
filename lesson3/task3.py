'''
Функція replace() може використовуватися для заміни будь-якого слова у рядку іншим словом.
Прочитайте кожен рядок зі створеного у попередньому завданні файлу learning_python.txt і замініть слово Python назвою іншої мови,
наприклад C при виведенні на екран. Це завдання написати в окремій функції.
'''


def reader():
    with open('possibilities.txt', 'r') as file1:
        file_lines = [x.strip() for x in file1.readlines()]
        for e in file_lines:
            n = e.replace('Python', 'C++')
            print(n)


if __name__ == '__main__':
    reader()
