"""
Створіть англо-німецький словник, який називається e2g, і виведіть його на екран.
Слова для словника: stork / storch, hawk / falke, woodpecker / specht і owl / eule.
Виведіть німецький варіант слова owl.
Додайте у словник, на ваш вибір, ще два слова та їхній переклад.
Виведіть окремо: словник; ключі і значення словника у вигляді списків.
"""

keys = ['stork', 'hawk', 'woodpecker', 'owl']
values = ['storch', 'falke', 'specht', 'eule']
e2g = dict(zip(keys, values))
e2g['day'] = 'tag'
e2g['night'] = 'nacht'
print(e2g, e2g.keys(), e2g.values())
