#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Древлеправославный старообрядческий 
календарь. 

"""

import datetime
from holidate_func import easter, ju_to_jd, weekday_ju, gr_to_jd
from menology import *

#Дни недели, месяцы, гласы.
weekday_word = {0: 'Воскресенье', 1: 'Понедельник', 2: 'Вторник', 3: 'Среда',
                4: 'Четверг', 5: 'Пятница', 6: 'Суббота'}

month_word = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня',
              7: 'июля', 8: 'августа', 9: 'сентября', 10: 'октября',
              11: 'ноября', 12: 'декабря'}

tone_word = {1: 'первый', 2: 'второй', 3: 'третий', 4: 'четвертый', 5: 'пятый',
             6: 'шестой', 7: 'седьмой', 0: 'восьмой'}


#Текущая дата по григорианскому календарю.
"""
gr_day = datetime.date.today().day
gr_month = datetime.date.today().month
gr_year = datetime.date.today().year
day, month, year = gr_to_jd(gr_day, gr_month, gr_year)



"""

gr_day = 26
gr_month = 10
gr_year = 2013
day, month, year = gr_to_jd(gr_day, gr_month, gr_year)

saint = menology[month][day]['saint']
bow = menology[month][day]['bow']

#Юлианская Дата Пасхи 
julian_date_easter = ju_to_jd(*easter(year))

#Юлианская дата текущего дня.
julian_date_today = ju_to_jd(day, month, year)

#Разница между Юлианской датой текущего дня и Юлианской датой Пасхи
difference_between_days = julian_date_today - julian_date_easter

#Текущий день недели.
#TODO: переписать используя datetime.
weekday = weekday_ju(day, month, year)

#Если текущая дата находится в периоде недели от Мытаря и фарисея, то 
#вычитаем Юлианскую дату будущей Пасхи из Юлианской даты текущего дня.
#Делим на 7, получаем неделю от Пасхи.
if difference_between_days >= -70:
    week_from_easter = (julian_date_today - (ju_to_jd(*easter(year)))) / 7
else:
    week_from_easter = (julian_date_today - (ju_to_jd(*easter(year - 1)))) / 7

#Неделя по 50-це.
week_after_pentecost = week_from_easter - 7

#Переходящие праздники.
if difference_between_days in [-70]:
    weekname = 'Неделя о мытаре и фарисее. Начало Триоди постной'
elif difference_between_days in range(-69, -63):
    weekname = 'Cедмица о мытаре и фарисее'
elif difference_between_days in [-63]:
    weekname = 'Неделя о блудном сыне'
elif difference_between_days in range(-62, -57):
    weekname = 'Седмица мясопустная'
elif difference_between_days in [-57]:
    weekname = 'Суббота мясопустная. Вселенское поминание усопших'
elif difference_between_days in [-56]:
    weekname = 'Неделя мясопустная. Воспоминание Страшного суда'
elif difference_between_days in range(-55, -50):
    weekname = 'Седмица сыропустная'
elif difference_between_days in [-50]:
    weekname = 'Суббота сыропустная. Память всех преподобных мужей и жен'
elif difference_between_days in [-49]:
    weekname = ('Неделя сыропустная. Воспоминание изгнания '
                'Адама и Еввы из рая')
elif difference_between_days in range(-48, -43):
    weekname = 'Первая седмица Великого поста'
elif difference_between_days in [-43]:
    weekname = 'Суббота Феодора Тирона'
elif difference_between_days in [-42]:
    weekname = 'Первая неделя Великого поста. Неделя Православия'
elif difference_between_days in range(-41, -34):
    weekname = 'Вторая седмица Великого поста'
elif difference_between_days in [-34]:
    weekname = 'Вторая суббота Великого поста. Поминание усопших'
elif difference_between_days in [-35]:
    weekname = ('Вторая неделя Великого поста. По уставу Успенского собора '
                'Московского Кремля совершается служба Федоровской '
                'иконе пресв. Богородицы')
elif difference_between_days in range(-34, -29):
    weekname = 'Третья седмица Великого поста'
elif difference_between_days in [-29]:
    weekname = 'Третья суббота Великого поста. Поминание усопших'
elif difference_between_days in [-28]:
    weekname = 'Третья неделя Великого поста. Поклонение Честному Кресту'
elif difference_between_days in range(-27, -22):
    weekname = 'Четвертая седмица Великого поста'
elif difference_between_days in [-22]:
    weekname = 'Третья суббота Великого поста. Поминание усопших'
elif difference_between_days in [-21]:
    weekname = 'Четвертая неделя Великого поста.  Иоанна Лествичника'
elif difference_between_days in range(-20, -15):
    if weekday in [1, 2, 3, 5]:
        weekname = 'Пятая седмица Великого поста'
    #TODO: Переписать, т.к. Марьино стояние меняется с Благовещением.
    elif weekday in [4]:
        weekname = ('Четверток Великого канона преп. Андрея Критского.  '
                    'Совершается служба Марьино стояние')
elif difference_between_days in [-15]:
    weekname = ('Пятая суббота Великого поста.  '
                'Служба Акафиста пресв. Богородицы.')
elif difference_between_days in [-14]:
    weekname = 'Пятая неделя Великого поста. Преп. Марьи Египетской'
elif difference_between_days in range(-13, -8):
    weekname = 'Шестая седмица Великого поста'
elif difference_between_days in [-8]:
    weekname = ('Воскрешение праведного Лазаря. Лазарева суббота.  '
                'Начало Триоди Цветной')
elif difference_between_days in [-7]:
    weekname = 'Вход Господень во Иерослаим. Неделя Ваий'
elif difference_between_days in [-6]:
    weekname = 'Начало Страстей Господних.  Великий понедельник'
elif difference_between_days in [-5]:
    weekname = 'Великий вторник'
elif difference_between_days in [-4]:
    weekname = 'Великая среда'
elif difference_between_days in [-3]:
    weekname = 'Великий четверг.  Воспоминание Тайной вечери'
elif difference_between_days in [-2]:
    weekname = 'Великий пяток'
elif difference_between_days in [-1]:
    weekname = 'Великая суббота'
elif difference_between_days in [0]:
    weekname = 'Пасха. Светлое Христово Воскресенье'
elif difference_between_days in range(1, 7):
    if weekday in [2]:
        weekname = ('Во вторник Светлой седмицы празднуем праздник  '
                    'Одигитрии пресв.  Богородицы')
    else:
        weekname = 'Светлая седмица'
elif difference_between_days in [7]:
    weekname = 'Неделя о Фоме. Антипасха'
elif difference_between_days in range(8, 14):
    if day in [9]:
        #TODO: Переписать, т. к. Радоница переносится,
        #если припадает в этот день Георгий Победоносец.
        weekname = ('Радоница. Во вторник второй седмицы по Пасхе '
                    'совершаем поминовение усопших')
    else:
        weekname = 'Седмица вторая по Пасхе о Фоме '
elif difference_between_days in [14]:
    weekname = ('Неделя третья по Пасхе свв. Жен Мироносиц  '
                'и Иосифа Праведного')
elif difference_between_days in range(15, 21):
    weekname = 'Седмица третья по Пасхе'
elif difference_between_days in [21]:
    weekname = 'Неделя о Расслабленном'
elif difference_between_days in range(22, 24):
    weekname = 'Седмица четвертая по Пасхе'
elif difference_between_days in [24]:
    weekname = 'Преполовение Пятидесятницы'
elif difference_between_days in range(25, 28):
    weekname = 'Седмица четвертая по Пасхе. Попраздненство Преполовения'
elif difference_between_days in [28]:
    weekname = 'Неделя о Самаряныни'
elif difference_between_days in range(29, 31):
    weekname = 'Седмица пятая по Пасхе. Попраздненство Преполовения'
elif difference_between_days in [31]:
    weekname = 'Отдание празника Преполовения'
elif difference_between_days in range(32, 35):
    weekname = 'Седмица пятая по Пасхе'
elif difference_between_days in [35]:
    weekname = 'Неделя о Слепом'
elif difference_between_days in range(36, 38):
    weekname = 'Седмица шестая по Пасхе'
elif difference_between_days in [38]:
    weekname = 'Отдание Пасхи'
elif difference_between_days in [39]:
    weekname = 'Вознесение Господне'
elif difference_between_days in range(40, 42):
    weekname = 'Попраздненство Вознесения. Седмица шестая по Пасхе'
elif difference_between_days in [42]:
    weekname = 'Неделя свв. Отцов первого Вселенского собора'
elif difference_between_days in range(43, 46):
    weekname = 'Попраздненство Вознесения. Седмица седьмая по Пасхе'
elif difference_between_days in [46]:
    weekname = 'Отдание праздника Вознесения'
elif difference_between_days in [47]:
    weekname = 'Седмица седьмая по Пасхе'
elif difference_between_days in [48]:
    weekname = ('В субботу седьмую по Пасхе совершаем память '
                'всем успопшим от века во Христа верующим '
                'отцам и братьям нашим')
elif difference_between_days in [49]:
    weekname = 'Пятидесятница. День святой Тройцы'
elif difference_between_days in [50]:
    weekname = 'Понедельник святого Духа'
elif difference_between_days in range(51, 55):
    weekname = 'Седмица первая по Пятидесятнице'
elif difference_between_days in [55]:
    weekname = 'Отдание праздника Пятидесятницы'
elif difference_between_days in [56]:
    weekname = 'Неделя всех святых'
else:
    if weekday in [0]:
        weekname = str(week_after_pentecost) + ' неделя по Пятидесятнице'
    elif weekday in [6]:
        weekname = str(week_after_pentecost) + ' суббота по Пятидесятнице'
    else:
        weekname = str(week_after_pentecost) + ' cедмица по Пятидесятнице'

# Правила для постов всего лета.
#От Недели о мытаре и фарисее до Недели о блудном сыне.
if difference_between_days in range(-70, -63):
    #Седмица сплошная, пища скоромная.
    fast = 7
#От Недели о блудном сыне до Недели мясопустной.
elif difference_between_days in range(-63, -56):
    if weekday in [0, 1, 2, 4, 6]:
        #Пища скоромная.
        if weekday in [0, 2, 4, 6] and saint in [1, 2, 3, 4, 5, 6]:
            fast = 7
        #Устав о трапезе, кто понедельничает.
        elif weekday in [1] and saint in [0]:
            fast = 8
        elif weekday in [1] and saint in [1, 2, 3]:
            fast = 9
        elif weekday in [1] and saint in [4, 5]:
            fast = 10
        elif weekday in [1] and saint in [6]:
            fast = 11
    #Устав о трапезе, в среду и в пяток.
    elif weekday in [3, 5] and saint in [0]:
        fast = 1
    elif weekday in [3, 5] and saint in [1, 2, 3]:
        fast = 2
    elif weekday in [3, 5] and saint in [4, 5]:
        fast = 3
    elif weekday in [3, 5] and saint in [6]:
        fast = 5
#От Недели мясопустной до Недели Сыропустной.
elif difference_between_days in range(-56, -48):
    #Седмица сплошная, на трапезе -- млеко, сыр, яйца.
    fast = 6
#От Недели сыропустной до первой недели Великого поста.
elif difference_between_days in range(-49, -42):
    #В первый и второй день Великого Поста.
    if weekday in [1, 2] and saint in [0, 1, 2, 3]:
        fast = 0
    # В первый и второй день Великого Поста
    #если полиелиос или Сретение.
    elif weekday in [1, 2] and saint in [4, 5, 6]:
        fast = 1
    elif weekday in [3, 4, 5] and saint in [0, 1, 2, 3]:
        fast = 1
    elif weekday in [3, 4, 5] and saint in [4, 5, 6]:
        fast = 2
    #В субботу Феодора Тирона.
    elif weekday in [6] and saint in [0, 1, 2, 3, 4, 5]:
        fast = 3
#От первой недели Великого поста
#до второй недели Великого поста.
elif difference_between_days in range(-42, -35):
    #В неделю Православия.
    if weekday in [0] and saint in [0, 1, 2, 3, 4, 5]:
        fast = 3
    #В понедельник, среду, пятницу.
    elif weekday in [1, 3, 5] and saint in [0, 1, 2, 3]:
        fast = 1
    #В понедельник, среду, пятницу если полиелиос.
    elif weekday in [1, 3, 5] and saint in [4, 5]:
        fast = 2
    #В понедельник, среду, пятницу если Благовешение.
    elif weekday in [1, 3, 5] and saint in [6]:
        fast = 5
    #Во вторник и четверг.
    elif weekday in [2, 4] and saint in [0, 1, 2, 3]:
        fast = 2
    #Во вторник и четверг если полиелиос.
    elif weekday in [2, 4] and saint in [4, 5]:
        fast = 3
    #Во вторник и четверг если Благовещение.
    elif weekday in [2, 4] and saint in [6]:
        fast = 5
    #В субботу вторую Великого поста.
    elif weekday in [6] and saint in [0, 1, 2, 3, 4, 5]:
        fast = 3
    #В субботу если Благовещенье.
    elif weekday in [6] and saint in [6]:
        fast = 5
#От второй недели Великого поста
#до третьей недели Великого поста.
elif difference_between_days in range(-35, -28):
    #В неделю Вторую.
    if weekday in [0] and saint in [0, 1, 2, 3, 4, 5]:
        fast = 3
    #В неделю если Благовещенье.
    elif weekday in [0] and saint in [6]:
        fast = 5
    #В понедельник, среду, пятницу.
    elif weekday in [1, 3, 5] and saint in [0, 1, 2, 3]:
        fast = 1
    #В понедельник, среду, пятницу если полиелиос.
    elif weekday in [1, 3, 5] and saint in [4, 5]:
        fast = 2
    #В понедельник, среду, пятницу если Благовешение.
    elif weekday in [1, 3, 5] and saint in [6]:
        fast = 5
    #Во вторник и четверг.
    elif weekday in [2, 4] and saint in [0, 1, 2, 3]:
        fast = 2
    #Во вторник и четверг если полиелиос.
    elif weekday in [2, 4] and saint in [4, 5]:
        fast = 3
    #Во вторник и четверг если Благовещение.
    elif weekday in [2, 4] and saint in [6]:
        fast = 5
    #В субботу третью Великого поста.
    elif weekday in [6] and saint in [0, 1, 2, 3, 4, 5]:
        fast = 3
    #В субботу третью если Благовещенье.
    elif weekday in [6] and saint in [6]:
        fast = 5
#От третьей недели Великого поста до четвертой недели Великого поста.
elif difference_between_days in range(-28, -21):
    #В неделю Крестопоклонную.
    if weekday in [0] and saint in [0, 1, 2, 3, 4, 5]:
        fast = 3
    #В неделю Крестопоклонную если Благовещенье.
    elif weekday in [0] and saint in [6]:
        fast = 5
    #В понедельник, среду, пятницу.
    elif weekday in [1, 3, 5] and saint in [0, 1, 2, 3]:
        fast = 1
    #В понедельник, среду, пятницу если полиелиос.
    elif weekday in [1, 3, 5] and saint in [4, 5]:
        fast = 2
    #В понедельник, среду, пятницу если Благовещение.
    elif weekday in [1, 3, 5] and saint in [6]:
        fast = 5
    #Во вторник и четверг.
    elif weekday in [2, 4] and saint in [0, 1, 2, 3]:
        fast = 2
    #Во вторник и четверг если полиелиос.
    elif weekday in [2, 4] and saint in [4, 5]:
        fast = 3
    #Во вторник и четверг если Благовещение.
    elif weekday in [2, 4] and saint in [6]:
        fast = 5
    #В субботу четвертую Великого поста.
    elif weekday in [6] and saint in [0, 1, 2, 3, 4, 5]:
        fast = 3
    #В субботу четвертую если Благовещенье.
    elif weekday in [6] and saint in [6]:
        fast = 5
#От четвертой недели Великого поста до пятой недели Великого поста.
elif difference_between_days in range(-21, -14):
    #В неделю Иоанна Лествичника.
    if weekday in [0] and saint in [0, 1, 2, 3, 4, 5]:
        fast = 3
    #В неделю Иоанна Лествичника если Благовещенье.
    elif weekday in [0] and saint in [6]:
        fast = 5
    #В понедельник, если Благовещение в четверг,
    #а Марьино стояние во вторник.
    elif weekday in [1] and day in [22] and saint in [0, 1, 2, 3]:
        fast = 2
    #В понедельник.
    elif weekday in [1] and saint in [1, 2, 3]:
        fast = 1
    #В понедельник, если полиелиос.
    elif weekday in [1] and saint in [4, 5]:
        fast = 2
    #В понедельник, если Благовещение.
    elif weekday in [1] and saint in [6]:
        fast = 5
    #Во вторник Марьино стояние, если Благовещение в четверг.
    elif weekday in [2] and day in [23] and saint in [0, 1, 2, 3, 4, 5]:
        fast = 3
    #Если 40 мученников попадают в четверг Великого канона, то он
    #переносится на вторник. Во вторник -- пища с маслом.
    elif weekday in [2] and day in [7] and saint in [0, 1, 2, 3]:
        fast = 3
    #Во вторник.
    elif weekday in [2] and saint in [0, 1, 2, 3]:
        fast = 2
    #Во вторник если полиелиос.
    elif weekday in [2] and saint in [4, 5]:
        fast = 3
    #Если Благовещение во вторник.
    elif weekday in [2] and saint in [6]:
        fast = 5
    #В среду.
    elif weekday in [3] and saint in [0, 1, 2, 3, 4, 5]:
        fast = 2
    #В среду, если Благовещение.
    elif weekday in [3] and saint in [6]:
        fast = 5
    #В четверг, Марьино стояние.
    elif weekday in [4] and saint in [0, 1, 2, 3, 4, 5]:
        fast = 3
    #В четверг, если Благовещение.
    elif weekday in [4] and saint in [6]:
        fast = 5
    #В пятницу.
    elif weekday in [5] and saint in [0, 1, 2, 3]:
        fast = 1
    #В пятницу, если полиелиос.
    elif weekday in [5] and saint in [4, 5]:
        fast = 2
    #В пятницу если Благовешение.
    elif weekday in [5] and saint in [6]:
        fast = 5
    #В субботу Акафиста.
    elif weekday in [6] and saint in [0, 1, 2, 3, 4, 5]:
        fast = 3
    #В субботу Акафиста, если Благовещение.
    elif weekday in [6] and saint in [6]:
        fast = 5
#От пятой недели Великого поста до Вербного воскресенья.
elif difference_between_days in range(-14, -7):
    #В неделю  преп. Марьи Египетской.
    if weekday in [0] and saint in [0, 1, 2, 3, 4, 5]:
        fast = 3
    #В неделю  преп. Марьи Египетской,
    #если Благовещение.
    elif weekday in [0] and saint in [6]:
        fast = 5
    #В понедельник, среду, пятницу.
    elif weekday in [1, 3, 5] and saint in [0, 1, 2, 3]:
        fast = 1
    #В понедельник, среду, пятницу если полиелиос.
    elif weekday in [1, 3, 5] and saint in [4, 5]:
        fast = 2
    #В понедельник, среду, пятницу если Благовешение.
    elif weekday in [1, 3, 5] and saint in [6]:
        fast = 5
    #Во вторник и четверг.
    elif weekday in [2, 4] and saint in [0, 1, 2, 3]:
        fast = 2
    #Во вторник и четверг если полиелиос.
    elif weekday in [2, 4] and saint in [4, 5]:
        fast = 3
    #Во вторник и четверг если Благовещение.
    elif weekday in [2, 4] and saint in [6]:
        fast = 5
    #В субботу вторую Великого поста.
    elif weekday in [6] and saint in [0, 1, 2, 3, 4, 5]:
        fast = 4
    #В субботу если Благовещенье.
    elif weekday in [6] and saint in [6]:
        fast = 5
#Страстная седмица.
elif difference_between_days in range(-7, 0):
    #В неделю Ваий.
    if weekday in [0] and saint in [0, 1, 2, 3, 4, 5, 6]:
        fast = 5
    #В Страстной понедельник,  вторник, среду.
    elif weekday in [1, 2, 3] and saint in [0, 1, 2, 3]:
        fast = 1
    #В Страстной понедельник, вторник, среду,
    #если полиелиос.
    elif weekday in [1, 2, 3] and saint in [4, 5]:
        fast = 1
    #В Страстной понедельник,  вторник, среду,
    #если Благовещение.
    elif weekday in [1, 2, 3] and saint in [6]:
        fast = 3
    #В Великий четверток.
    elif weekday in [4] and saint in [0, 1, 2, 3, 4, 5]:
        fast = 14
    #В Великий четверток, если Благовещение.
    elif weekday in [4] and saint in [6]:
        fast = 3
    #В Великий пяток и Великую субботу
    #трапеза не поставляется.
    elif weekday in [5, 6] and saint in [0, 1, 2, 3, 4, 5]:
        fast = 0
    #В Великий пяток и Великую субботу,
    #если Благовещение.
    elif weekday in [5, 6] and saint in [6]:
        fast = 2
#Светлая седмица.
elif difference_between_days in range(0, 7):
    #Седмица сплошная, пища скоромная.
    fast = 7
#От Недели Фоминой до Пятидесятницы.
elif difference_between_days in range(7, 50):
    #Неделя Фомина и другие недели.
    if weekday in [0] and saint in [0, 1, 2, 3, 4, 5]:
        fast = 7
    #В для тех кто постится в понедельник.
    elif weekday in [1] and saint in [0, 1, 2, 3, 4, 5]:
        fast = 11
    #Во вторник, четверг, субботу.
    elif weekday in [2, 4, 6] and saint in [0, 1, 2, 3, 4, 5]:
        fast = 7
    #В среду, пятницу.
    elif weekday in [3, 5] and saint in [0, 1, 2, 3, 4, 5]:
        fast = 5
#Сплошная седмица от Пятидесятницы до недели Всех святых.
elif difference_between_days in range(50, 58):
#Седмица сплошная, пища скоромная.
    fast = 7
#Петров пост.
elif julian_date_today in range(julian_date_easter + 57, ju_to_jd(29, 6, year)):
#В понедельник, среду, пятницу сухоядение,
#если святой на 4.
    if weekday in [1, 3, 5] and saint in [0]:
        fast = 1
        #В понедельник, среду, пятницу
        #пища без масла, если святой на 6 или полиелеос.
    elif weekday in [1, 3, 5] and saint in [0, 1, 2, 3, 4]:
        fast = 2
        #В понедельник, среду, пятницу
        #пища с маслом, если бдение.
    elif weekday in [1, 3, 5] and saint in [5]:
        fast = 3
        #В понедельник, среду, пятницу
        #на трапезе рыба, если Рождество Иоанна Предотечи.
    elif weekday in [1, 3, 5] and saint in [6]:
        fast = 5
        #Во вторник, четверг, субботу, неделю,
        #на трапезе рыба.
    elif weekday in [0, 2, 4, 6] and saint in [0, 1, 2, 3, 4, 5, 6]:
        fast = 5
#Мясоед от дня свв. апп. Петра и Павла до праздника происхождения Креста.
elif julian_date_today in range(ju_to_jd(29, 6, year), ju_to_jd(1, 8, year)):
#Неделя, вторник, четверг, суббота.
    if weekday in [0, 2, 4, 6] and saint in [0, 1, 2, 3, 4, 5, 6]:
        fast = 7
    #В для тех кто постится в понедельник.
    elif weekday in [1] and saint in [0, 1]:
        fast = 9
        #В для тех кто постится в понедельник,
        #когда Славословие и Полиелеос.
    elif weekday in [1] and saint in [2, 3, 4, 5]:
        fast = 10
    #Великобденный в понедельник.
    elif weekday in [1] and saint in [6]:
        fast = 11
    #Среда, пятница.
    elif weekday in [3, 5] and saint in [0, 1]:
        fast = 2
        #когда Славословие и Полиелеос.
    elif weekday in [3, 5] and saint in [2, 3, 4, 5]:
        fast = 3
    #Великобденный в среду, пятницу.
    elif weekday in [3, 5] and saint in [6]:
        fast = 5
#Успенский пост.
elif julian_date_today in range(ju_to_jd(1, 7, year), ju_to_jd(15, 8, year)):
#В понедельник, среду, пятницу сухоядение,
#если святой на 4.
    if weekday in [1, 3, 5] and saint in [0]:
        fast = 1
        #В понедельник, среду, пятницу
        #пища без масла, если святой на 6 или полиелеос.
    elif weekday in [1, 3, 5] and saint in [1, 2, 3, 4]:
        fast = 2
        #В понедельник, среду, пятницу
        #пища с маслом, если бдение.
    elif weekday in [1, 3, 5] and saint in [5]:
        fast = 3
        #Во вторник, четверг, субботу, неделю,
        #на трапезе масло.
    elif weekday in [0, 2, 4, 6] and saint in [0, 1, 2, 3, 4, 5]:
        fast = 5
    #Рыба на Преображение.
    elif weekday in [0, 1, 2, 3, 4, 5, 6] and saint in [6]:
        fast = 5
#Усекновение.
elif julian_date_today == ju_to_jd(29, 8, year):
    fast = 3
#Воздвижение.
elif julian_date_today == ju_to_jd(14, 9, year):
    fast = 3
#Мясоед от праздника Успения до памяти ап. Филиппа.
elif julian_date_today in range(ju_to_jd(15, 8, year), ju_to_jd(14, 11, year)):
#Неделя, вторник, четверг, суббота.
    if weekday in [0, 2, 4, 6] and saint in [0, 1, 2, 3, 4, 5, 6]:
        fast = 7
    #Для тех кто постится в понедельник.
    elif weekday in [1] and saint in [0, 1]:
        fast = 9
        #В для тех кто постится в понедельник,
        #когда славословие и полиелеос.
    elif weekday in [1] and saint in [2, 3, 4]:
        fast = 10
    #Бденный, великобденный в понедельник.
    elif weekday in [1] and saint in [5, 6]:
        fast = 11
    #Среда, пятница.
    elif weekday in [3, 5] and saint in [0, 1]:
        fast = 2
        #когда славословие и полиелеос, Бдение.
    elif weekday in [3, 5] and saint in [2, 3, 4, 5]:
        fast = 3
    #Великобденный в среду, пятницу.
    elif weekday in [3, 5] and saint in [6]:
        fast = 5
#От дня ап. Филиппа до дня свт. Николы.
elif julian_date_today in range(ju_to_jd(14, 11, year), ju_to_jd(6, 12, year)):
#В понедельник, среду, пятницу сухоядение,
#если святой на 4.
    if weekday in [1, 3, 5] and saint in [0]:
        fast = 1
        #В понедельник, среду, пятницу
        #пища без масла, если святой на 6 или полиелеос.
    elif weekday in [1, 3, 5] and saint in [0, 1, 2, 3, 4]:
        fast = 2
        #В понедельник, среду, пятницу
        #пища с маслом, если бдение.
    elif weekday in [1, 3, 5] and saint in [5]:
        fast = 3
        #Введение Пресвятой Богородицы,
        #на трапезе рыба.
    elif weekday in [1, 3, 5] and saint in [6]:
        fast = 5
        #Во вторник, четверг, субботу, неделю,
        #на трапезе рыба.
    elif weekday in [0, 2, 4, 6] and saint in [0, 1, 2, 3, 4, 5, 6]:
        fast = 5
#Навечерие Рождества.
elif julian_date_today == ju_to_jd(24, 12, year):
#В будние дни пища без масла.
    if weekday in [1, 2, 3, 4, 5] and saint in [0, 1, 2, 3, 4, 5]:
        fast = 2
    #В субботу, неделю пища с маслом.
    elif weekday in [0, 6] and saint in [0, 1, 2, 3, 4, 5]:
        fast = 3
#От дня свт. Николы до Рождества.
elif julian_date_today in range(ju_to_jd(6, 12, year), ju_to_jd(25, 12, year)):
#В понедельник, среду, пятницу сухоядение,
#если святой на 4.
    if weekday in [1, 3, 5] and saint in [0]:
        fast = 1
        #В понедельник, среду, пятницу
        #пища без масла, если святой на 6 или полиелеос.
    elif weekday in [1, 3, 5] and saint in [0, 1, 2, 3, 4]:
        fast = 2
        #В понедельник, среду, пятницу
        #пища с маслом, если бдение.
    elif weekday in [1, 3, 5] and saint in [5]:
        fast = 3
        #В субботу, неделю
        #на трапезе рыба.
    elif weekday in [0, 6] and saint in [0, 1, 2, 3, 4, 5, 6]:
        fast = 5
#Навечерие Богоявления.
elif julian_date_today == ju_to_jd(5, 1, year):
#В будние дни пища без масла.
    if weekday in [1, 2, 3, 4, 5] and saint in [0, 1, 2, 3, 4, 5]:
        fast = 2
    #В субботу, неделю пища с маслом.
    elif weekday in [0, 6] and saint in [0, 1, 2, 3, 4, 5]:
        fast = 3
#Святки.
elif julian_date_today in range(ju_to_jd(25, 12, year), ju_to_jd(31, 12, year) + 1):
    fast = 7
elif julian_date_today in range(ju_to_jd(1, 1, year), ju_to_jd(7, 1, year)):
    fast = 7
#От Крещения Господня до Недели о мытаре и фарисее.
else:
    #В неделю, вторник, четверг, субботу.
    if weekday in [0, 2, 4, 6] and saint in [0, 1, 2, 3, 4, 5, 6]:
        fast = 7
    #В для тех кто постится в понедельник.
    elif weekday in [1] and saint in [0, 1, 2, 3, 4, 5, 6]:
        fast = 11
    #В среду, пятницу.
    elif weekday in [3, 5] and saint in [0, 1, 2, 3, 4, 5, 6]:
        fast = 5

#Устав Гласов во все Лето.
#Светлая седмица.
if difference_between_days in range(0, 6):
    tone = weekday + 1
elif difference_between_days in [6]:
    tone = 8
else:
    if difference_between_days < -8 and month in [1, 2, 3, 4]:
        tone = ((julian_date_today - (ju_to_jd(*easter(year - 1)))) / 7) % 8
    elif difference_between_days > 6:
        tone = ((julian_date_today - (ju_to_jd(*easter(year)))) / 7) % 8

#Устав о приходных и исходных полонах всего лета.
#В неделю Сыропустную.
if difference_between_days in [-49]:
    bows = ('Утром, на службе приходные и исходные поклоны  поясные, '
            'а вечером -- приходные поясные, исходные земные')
#Устав на полиелеосы в Великий Пост.
elif difference_between_days in range(-49, 0):
    if weekday in [5]:
        if bow in [2, 3, 4, 5]:
            bows = 'Приходные и исходные поклоны земные'
        elif weekday in [5] and bow in [2, 3, 4, 5]:
            bows = ('Утром, на службе приходные и исходные поклоны  земные, '
                    'а вечером -- приходные и исходные поясные')
        #В неделю.
        elif weekday in [0] and bow in [2, 3, 4, 5]:
            bows = ('Утром, на службе приходные и исходные поклоны  поясные, '
                    'а вечером -- приходные поясные, исходные земные')
        elif weekday in [5] and bow in [2, 3, 4, 5]:
            bows = ('Утром, на службе приходные и исходные поклоны  земные, '
                    'а вечером -- приходные и исходные поясные')
        elif weekday in [0] and bow in [2, 3, 4, 5]:
            bows = ('Утром, на службе приходные и исходные поклоны  поясные, '
                    'а вечером -- приходные поясные, исходные земные')
    #В неделю.
    elif weekday in [0]:
        #Если нет попразненства,
        #утром, на службе приходные и
        #поклоны  поясные,
        #а вечером -- приходные поясные,
        #исходные земные.
        if bow in [0, 1, 2, 3]:
            bows = ('Утром, на службе приходные и исходные поклоны  поясные, '
                    'а вечером -- приходные поясные, исходные земные')
            #Попраздненство: приходные
        #и исходные поясные с утра и вечером.
    elif bow in [5]:
        bows = 'Приходные и исходные поклоны поясные'
    #В субботу поклоны поясные.
    elif weekday in [6]:
        #Кроме Великой  субботы.
        if difference_between_days in [-1]:
            bows = 4
        else:
            bows = 'Приходные и исходные поклоны поясные'
#От Пасхи до недели Всех Святых.
#поклоны поясные.
elif difference_between_days in range(0, 58):
    bows = 'Приходные и исходные поклоны поясные'
#Когда нет Триоди.
else:
    #В воскресенье.
    if weekday in [0]:
        bows = 'Приходные и исходные поклоны поясные'
    #Среди седмицы во все двунадесятые, бденные,
    #полиелеосные праздники,
    #когда выход и славословие,
    #а также в попраздненства поклоны поясные.
    elif weekday in [1, 2, 3, 4]:
        #12-й праздник и попраздненство.
        if bow in [4, 5]:
            bows = 'Приходные и исходные поклоны поясные'
        #Бдение.
        elif bow in [3]:
            bows = ('Утром, на службе приходные и исходные поклоны  поясные, '
                    'а вечером -- приходные поясные, исходные земные' )
        #Славословие и полиелеос.
        elif bow in [1, 2]:
            bows = ('Утром, на службе приходные и исходные поклоны  поясные, '
                    'а вечером -- приходные и исходные земные')
        #Когда святой на 4 или на 6,
        #и нет попразненства.
        elif bow in [0]:
            bows = 'Приходные и исходные поклоны земные'
    #В пятницу.
    elif weekday in [5]:
        #Когда святой на 4 или на 6,
        #и нет попразненства --
        #приходные земные, исходные поясные.
        if bow in [0]:
            bows = 'Приходные поклоны земные, а исходные поклоны поясные'
        #Бдение, полиелеос, 12-й праздник,
        #попраздненство.
        elif bow in [2, 3, 4, 5]:
            bows = 'Приходные и исходные поклоны поясные'
    #В субботу.
    elif weekday in [6]:
        bows = 'Приходные и исходные поклоны поясные'


fasts_word = {
    0: 'Трапеза не поставляется',
    1: 'Сухоядение',
    2: 'Пища без масла',
    3: 'Пища с маслом',
    4: 'Пища с икрой',
    5: 'Пища с рыбой',
    6: 'На трапезе -- молоко, сыр, яйца',
    7: 'Пища скоромная',
    8: 'Для постящихся в понедельник -- сухоядение, для остальных -- пища скоромная',
    9: 'Для постящихся в понедельник -- пища без масла, для остальных -- пища скоромная',
    10: 'Для постящихся в понедельник -- пища с маслом, для остальных -- пища скоромная',
    11: 'Для постящихся в понедельник -- пища с рыбой,  для остальных -- пища скоромная',
    12: 'На трапезе -- молоко, сыр, яйца',
    13: 'Пища скоромная',
    14: 'Пища без масла, пьем вино ради восопминания Вечери Господней'
    }

print '******************************************************'

print weekname,
print ''
print 'Глас', tone_word[tone]
print ''
# Вывод дня недели.
print weekday_word[weekday]
# Дата по юлианскому календарю.
print day, month_word[month], year, 'года', '-- По юлианскому календарю'
print gr_day, month_word[gr_month], gr_year, 'года', '-- По григорианскому календарю'
print ''
# Вывод дня недели.
print menology[month][day]['first_saint'],
try:
    print menology[month][day]['second_saint'], menology[month][day]['old_believer_saint']
except KeyError:
    None
print fasts_word[fast] + '.'
print ' '
#Поклоны
print bows + '.'
print ''
print '****************Служебная***************************'
print 'Пасха:', easter(year)
print 'Юлианская дата Пасхи:', julian_date_easter
print 'Юлианская дата текущего дня:', julian_date_today

print '******************************************************'
