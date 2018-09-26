"""
Cтворіть словник з трьома річками і регіонами, територією яких вони протікають.
Одна з можливих пар «ключ: значення» - 'Amazon': 'South America'. Додайте ще дві пари «річка: регіон» у словник.
Виведіть повідомлення із назвами річки і регіону - наприклад,
«The Amazon runs through South America.»
для усіх елементів словника, враховуючи те, що у повідомлення у відповідні місця підставляються назви річок і територій.
( використати створення функції і метод format )
"""

river = {
    'Amazon': 'South America',
    'Poltva': 'Europe',
    'Nill': 'Egept'
}

river['Dnipro'] = 'Europe'
river['Sena'] = 'Europe'

for key in river:
    print('The {} runs through {}.'.format(key, river[key]))
