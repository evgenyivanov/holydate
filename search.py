#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Поиск имен святых в календаре.

"""
import datetime
from menology import menology
from holidate_func import ju_to_gr_in_search

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

search_string = 'Спиридон'
d = menology
out = []
year = datetime.date.today().year

#Ищем в menology строку; если есть, добавляем в словарь.
for key, value in d.iteritems():
    for key1, value1 in d[key].iteritems():
        for key2, value2 in d[key][key1].iteritems():
            if search_string in str(value2):
                out.extend([[ju_to_gr_in_search(key1, key, year), [key1, key], [value2]]])

#Меняем элементы вложенного списка на значения словаря с названиями месяцев.
for item in out:
    item[0][1], item[1][1] = month_word[item[0][1]], month_word[item[1][1]]

#Вывод результата.
#TODO: обработать вывод, если строка поиска не найдена.
for item in out:
    print item[0][0], item[0][1], 'по ст. ст.', '\n', item[1][0], item[1][1], 'по н. ст.', item[2][0]

