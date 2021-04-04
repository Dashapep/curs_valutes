# прочесть из ком.строки название jsonфайла и название отдела
# выводить надо в порядке убывания количества сотрудников + отделы по алфавиту

import json
import sys

param = sys.argv
# считать имя файла их командной строки
with open(param[1], 'r', encoding='utf8') as comp_file:
    data = json.load(comp_file)
st = ' '.join(param[2:]) # собрать название отдела из нескольких слов
# Подсчет колва сотрудников в отделах
dct = {}
# for i in data['users']:  # выпадет ошибка  KeyError, если нет ключа
for i in data.get('users'): # результат- None, если нет ключа
    otdel = i['department']
    if otdel == st: # python size.py comp.json Бухгалтерия . Посчитать кол-во сотрудников
        if otdel not in dct:
            dct[otdel] = 1
        else:
            dct[otdel] += 1
# Вывести название отделов и количество сотрудников в  этом отделах.
#  Приведем словарь {"Отдел продаж": 4, ...} в список кортежей вида [('Отдел продаж', 4), ...]
spis = []
for key, value in dct.items():
    spis.append((key, value))
# Сортировка списка по двум параметрам по возрастаию, но числа по убыванию
spis.sort(key=lambda y: (-y[1], y[0]), reverse=False)
# Вывод
for i in spis:
    print(i[0], i[1])

# Вывести названия отделов и количество сотрудников в  этих отделах.
with open('cats_2.json', 'r', encoding='utf8') as comp_file:
    data = json.load(comp_file)
# Подсчет колва сотрудников в отделах
dct = {}
for i in data['users']:
    otdel = i['department']
    if otdel not in dct:
        dct[otdel] = 1
    else:
        dct[otdel] += 1
#  Приведем словарь {"Отдел продаж": 4, ...} в список кортежей вида [('Отдел продаж', 4), ...]
spis = []
for key, value in dct.items():
    spis.append((key, value))
# Сортировка списка по двум параметрам по возрастаию, но числа по убыванию
spis.sort(key=lambda y: (-y[1], y[0]), reverse=False)
# Вывод
for i in spis:
    print(i[0], i[1])

male = 0
female = 0
for i in data['users']:
    if i['gender'] == "male":
        male += 1
    elif i["gender"] == 'female':
        female += 1
print('на 23:', male, ", а на 8:", female)


