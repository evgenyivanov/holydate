#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Поиск имен святых в календаре.

"""

from menology import menology

month_word = {
    1: 'января',
    2: 'февраля',
    3: 'марта',
    4: 'апреля',
    5: 'мая',
    6: 'июня',
    7: 'июля',
    8: 'августа',
    9: 'сентября',
    10: 'октября',
    11: 'ноября',
    12: 'декабря'
}

search_string = 'Рожество'
d = menology
list_result = []

#Ищем в menology строку; если есть, добавляем в словарь.
for key, value in d.iteritems():
    for key1, value1 in d[key].iteritems():
        for key2, value2 in d[key][key1].iteritems():
            if search_string in str(value2):
                list_result.extend([[key, [key1, value2]]])

#Меняем 0 элемент вложенного списка на значения словаря с названиями месяцев.
out = map(lambda s: s[0] in month_word and [month_word[s[0]], s[1]] or s, list_result)

#Вывод результата.
for index, item in out:
    print item[0], index, 'по ст. ст.', item[1]

