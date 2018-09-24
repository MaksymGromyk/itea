#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
.Створіть новий словник під назвою prices за допомогою {}
.Покладіть в словник такі значення "banana": 4, "apple": 2, "orange": 1.5, "pear": 3
.Створити новий словник stocks.( який буде містити інформацію для кожного ключа із prices скільки товару ( запасу є на складі).
Згенерувати значення випадковим чином.
.Проітеруйтесь в циклі  через кожен  ключ  в prices. Для кожного ключа надрукуйте ключ разом із ціною, а також запасом на складі.
Надрукуйте відповідь у наступному форматі:
apple
price: 2
stock: 5
.Давайте визначимо, скільки грошей ви зробили б, якщо б ви продали всю їжу ( змінна total, треба вирахувати і надрукувати її )
"""
from random import randint

prices = {}
keys = ("banana", "apple", "orange", "pear")
values = (4, 2, 1.5, 3)
# for k, n in keys, range(len(values)):
#     prices[k] = values[n]
n = 0

for k in keys:
    prices[k] = values[n]
    n += 1
stocks = {}
keys = [e for e in prices.keys()]
values = [randint(0, 10000) for i in range(len(prices))]

for e, n in zip(keys, values):
    stocks[e] = n
for key in prices.keys():
    print('{}\nprice: {}\nstock: {}\n'.format(key, prices[key], stocks[key]))
total = sum([prices[k] * stocks[k] for k in prices.keys()])
print(total)
