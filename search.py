#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Поиск имен святых.

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

search_string = 'Николы'
d = menology
dict_result = {}

#Ищем в menology строку; если есть, добавляем в словарь.
for key, value in d.iteritems():
    for key1, value1 in d[key].iteritems():
        for key2, value2 in d[key][key1].iteritems():
            if search_string in str(value2):
                dict_result.setdefault(key, {}).update({key1: value2})

#Меням key на строки с названиями месяцев.
out = {}
for key, value in month_word.iteritems():
    try:
        out.setdefault(value, dict_result[key])
    except KeyError:
        continue

#Вывод результата.
for key, value in out.iteritems():
    for key1, value2 in out[key].iteritems():
        print key1, key, value2











