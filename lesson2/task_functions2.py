"""
Написати функцію random_from_list, яка приймає список слів, і вертає те слово, яке є найдовшим.
"""


# def random_from_list(list_of_words):
#     if len(list_of_words) > 1:
#         for e in list_of_words:
#             if len(e[0]) > len(e[1]):
#                 del list_of_words[1]
#             else:
#                 del list_of_words[0]
#             return list_of_words


def random_1(li):
    return max(li, key=len)


if __name__ == '__main__':
    list_of_words = input('Please type after the dot the words that you want to compate\n . ').split()
    print(random_1(list_of_words))
