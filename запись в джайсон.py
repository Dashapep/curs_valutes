# Вывести названия отделов и количество сотрудников в  этих отделах.
# выводить надо в порядке убывания количества сотрудников + отделы по алфавиту

import json

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

# ensure_ascii=False - чтобы при записи в файл бали русские буквы

# создать и записать в новый json файл сотрудников, рожденных до 2000
slov = {}
with open('new_comp.json', 'w', encoding='utf8') as nc_file:
    for i in data['users']:
        birth = i['birthDate'].split('.')
        if int(birth[2]) < 2000:
            slov[i['firstName'] + " " + i['lastName']] = i['birthDate']
    json.dump(slov, nc_file, ensure_ascii=False)

# {"Татьяна Моисейкина": "10.29.1980", ...


