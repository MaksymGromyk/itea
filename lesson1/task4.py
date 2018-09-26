#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Спробуйте зробити наступне:
     4a)    Додайте ключ до словника під назвою "pocket".
     4b)    Встановіть значення "pocket" як список, що складається з рядків 'seashell', 'strange berry', і  'lint’
     4с)    Відсортуйте ( .sort ()) елементи зі списку, що зберігаються під ключем  "backpack". ( і надрукуйте)
     4d)    Потім видаліть ("dagger") зі списку предметів, що зберігаються під ключем “backpack".
    4e)     Додайте 50 до числа, збереженого під "gold" ключем. І надрукуйте результат.
5)
'''


inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['pocket'] = None
inventory['pocket'] = sorted(['seashell', 'strange berry', 'lint'])
print(inventory['backpack'])
del inventory['backpack'][1]
inventory['gold'] += 50
print(inventory)
