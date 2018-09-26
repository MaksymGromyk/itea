'''
Завантажте текстову версію однієї з книг із сайту Project Gutenberg’s.
Замініть усі розриви рядків у тексті символом пропуску і запишіть відформатований текст у новий файл formatted_text.txt.
'''


with open('book.txt', 'r') as book:
    text = book.read().replace('\n', ' ')
    print(text)
