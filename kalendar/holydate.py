#!/usr/bin/env python
# coding: utf-8

""" Holydate -- the ancient orthodox calendar.

holydate.main
~~~~~~~~~~~~~

This module represent oldbeliever orthodox calendar.

:copyright: 2014 by Maxim Chernytevich.
:license: GPLv2, see LICENSE for more details.

"""
from menology import menology
from holydate_func import easter, gr_to_ju, ju_to_jd, gr_to_jd, weekday_ju


class AncientCalendar:

    """ Ancient orthodox Calendar. """

    def __init__(self, gr_day, gr_month, gr_year):

        self.gr_day = gr_day
        self.gr_month = gr_month
        self.gr_year = gr_year
        self.day, self.month, self.year = gr_to_jd(gr_day, gr_month, gr_year)

        self.saint = menology[self.month][self.day]['saint']
        self.bow = menology[self.month][self.day]['bow']
        #Julian calendar date of Easter.
        self.julian_date_easter = ju_to_jd(*easter(self.year))
        #Julian calendar date day.
        self.julian_date_today = ju_to_jd(self.day, self.month, self.year)
        #Разница между Юлианской датой текущего дня и Юлианской датой Пасхи
        self.difference_between_days = self.julian_date_today - self.julian_date_easter
        #Текущий день недели.
        self.weekday = weekday_ju(self.day, self.month, self.year)

        #Если текущая дата находится в периоде недели от Мытаря и фарисея, то
        #вычитаем Юлианскую дату будущей Пасхи из Юлианской даты текущего дня.
        #Делим на 7, получаем неделю от Пасхи.
        if self.difference_between_days >= -70:
            self.week_from_easter = (self.julian_date_today - (ju_to_jd(*easter(self.year)))) / 7
        else:
            self.week_from_easter = (self.julian_date_today - (ju_to_jd(*easter(self.year - 1)))) / 7
        #Неделя по 50-це.
        self.week_after_pentecost = self.week_from_easter - 7

    def getTone(self):
        """Get Tone for day."""

        #Светлая седмица.
        if self.difference_between_days in range(0, 6):
            self.tone = self.weekday + 1
        elif self.difference_between_days in [6]:
            self.tone = 8
        else:
            if self.difference_between_days < -8 and self.month in [1, 2, 3, 4]:
                self.tone = ((self.julian_date_today - (ju_to_jd(*easter(self.year - 1)))) / 7) % 8
            elif self.difference_between_days > 6:
                self.tone = ((self.julian_date_today - (ju_to_jd(*easter(self.year)))) / 7) % 8
        self.tone_word = {
            1: 'первый',
            2: 'второй',
            3: 'третий',
            4: 'четвертый',
            5: 'пятый',
            6: 'шестой',
            7: 'седьмой',
            0: 'восьмой'
        }

        return 'Глас ' + self.tone_word[self.tone]

    def getWeekdayname(self):
        """Names of weekday for all the year."""

        #Переходящие праздники.
        if self.difference_between_days in [-70]:
            self.weekdayname = '{red}Неделя о Мытаре и Фарисее. Начало Триоди постной.{end}'
        elif self.difference_between_days in range(-69, -63):
            self.weekdayname = 'Cедмица о Мытаре и Фарисее.'
        elif self.difference_between_days in [-63]:
            self.weekdayname = '{red}Неделя о Блудном сыне.{end}'
        elif self.difference_between_days in range(-62, -57):
            self.weekdayname = 'Седмица Мясопустная.'
        elif self.difference_between_days in [-57]:
            self.weekdayname = 'Суббота Мясопустная. Вселенское поминание усопших.'
        elif self.difference_between_days in [-56]:
            self.weekdayname = '{red}Неделя Мясопустная. Воспоминание Страшного суда.{end}'
        elif self.difference_between_days in range(-55, -50):
            self.weekdayname = 'Седмица Cыропустная.'
        elif self.difference_between_days in [-50]:
            self.weekdayname = '{red}Суббота Cыропустная. Память всех преподобных мужей и жен (Сл.).{end}'
        elif self.difference_between_days in [-49]:
            self.weekdayname = ('{red}Неделя сыропустная. Воспоминание изгнания '
                                'Адама и Еввы из рая.{end}')
        elif self.difference_between_days in range(-48, -43):
            self.weekdayname = 'Первая седмица Великого поста.'
        elif self.difference_between_days in [-43]:
            self.weekdayname = 'Суббота Феодора Тирона.'
        elif self.difference_between_days in [-42]:
            self.weekdayname = '{red}Первая неделя Великого поста. Неделя Православия.{end}'
        elif self.difference_between_days in range(-41, -34):
            self.weekdayname = 'Вторая седмица Великого поста.'
        elif self.difference_between_days in [-34]:
            self.weekdayname = 'Вторая суббота Великого поста. Поминание усопших.'
        elif self.difference_between_days in [-35]:
            self.weekdayname = ('{red}Вторая неделя Великого поста. По уставу Успенского собора '
                                'Московского Кремля совершается служба Федоровской '
                                'иконе пресв. Богородицы.{end}')
        elif self.difference_between_days in range(-34, -29):
            self.weekdayname = 'Третья седмица Великого поста.'
        elif self.difference_between_days in [-29]:
            self.weekdayname = 'Третья суббота Великого поста. Поминание усопших.'
        elif self.difference_between_days in [-28]:
            self.weekdayname = '{red}Третья неделя Великого поста. Поклонение Честному Кресту.{end}'
        elif self.difference_between_days in range(-27, -22):
            self.weekdayname = 'Четвертая седмица Великого поста.'
        elif self.difference_between_days in [-22]:
            self.weekdayname = 'Третья суббота Великого поста. Поминание усопших.'
        elif self.difference_between_days in [-21]:
            self.weekdayname = '{red}Четвертая неделя Великого поста. Иоанна Лествичника.{end}'
        elif self.difference_between_days in range(-20, -15):
        #Марьино стояние меняется с Благовещением.
            if self.weekday in [2] and self.day in [23] and self.month in [3]:
                self.weekdayname = ('Четверток Великого канона преп. Андрея Критского.  '
                                    'Совершается служба Марьино стояние.')
            elif self.weekday in [1, 2, 3, 5]:
                self.weekdayname = 'Пятая седмица Великого поста.'
            #Марьино стояние меняется с Благовещением.
            elif self.weekday in [4] and self.day in [25] and self.month in [3]:
                self.weekdayname = 'Пятая седмица Великого поста.'
            elif self.weekday in [4]:
                self.weekdayname = ('Четверток Великого канона преп. Андрея Критского.  '
                                    'Совершается служба Марьино стояние.')
        elif self.difference_between_days in [-15]:
                self.weekdayname = ('{red}Пятая суббота Великого поста.  '
                                    'Служба Акафиста пресв. Богородицы (Сл.).{end}')
        elif self.difference_between_days in [-14]:
            self.weekdayname = '{red}Пятая неделя Великого поста. Преп. Марьи Египетской.{end}'
        elif self.difference_between_days in range(-13, -8):
            self.weekdayname = 'Шестая седмица Великого поста.'
        elif self.difference_between_days in [-8]:
            self.weekdayname = ('{red}Воскрешение праведного Лазаря. Лазарева суббота (Сл.).  '
                                'Начало Триоди Цветной.{end}')
        elif self.difference_between_days in [-7]:
            self.weekdayname = '{red}⊕ Вход Господень во Иерослаим. Неделя Ваий.{end}'
        elif self.difference_between_days in [-6]:
            self.weekdayname = 'Начало Страстей Господних. Великий понедельник.'
        elif self.difference_between_days in [-5]:
            self.weekdayname = 'Великий вторник.'
        elif self.difference_between_days in [-4]:
            self.weekdayname = 'Великая среда.'
        elif self.difference_between_days in [-3]:
            self.weekdayname = '{red}Великий четверг. Воспоминание Тайной вечери.{end}'
        elif self.difference_between_days in [-2]:
            self.weekdayname = 'Великий пяток.'
        elif self.difference_between_days in [-1]:
            self.weekdayname = 'Великая суббота.'
        elif self.difference_between_days in [0]:
            self.weekdayname = '{red}⊕ Пасха. Светлое Христово Воскресенье.{red}'
        elif self.difference_between_days in range(1, 7):
            if self.weekday in [2]:
                self.weekdayname = ('{red}☩ Во вторник Светлой седмицы празднуем праздник  '
                                    'Одигитрии пресв. Богородицы.{end}')
            else:
                self.weekdayname = '{red}Светлая седмица.{end}'
        elif self.difference_between_days in [7]:
            self.weekdayname = '{red}Неделя о Фоме. Антипасха.{end}'
        elif self.difference_between_days in range(8, 14):
            if self.day in [9]:
                #TODO: Переписать, т. к. Радоница переносится,
                #если припадает в этот день Георгий Победоносец.
                self.weekdayname = ('Радоница. Во вторник второй седмицы по Пасхе '
                                    'совершаем поминовение усопших')
            else:
                self.weekdayname = 'Седмица вторая по Пасхе о Фоме.'
        elif self.difference_between_days in [14]:
            self.weekdayname = ('{red}Неделя третья по Пасхе свв. Жен Мироносиц  '
                                'и Иосифа Праведного.{end}')
        elif self.difference_between_days in range(15, 21):
            self.weekdayname = 'Седмица третья по Пасхе'
        elif self.difference_between_days in [21]:
            self.weekdayname = '{red}Неделя о Расслабленном.{end}'
        elif self.difference_between_days in range(22, 24):
            self.weekdayname = 'Седмица четвертая по Пасхе.'
        elif self.difference_between_days in [24]:
            self.weekdayname = '{red}Преполовение Пятидесятницы (Сл.).{end}'
        elif self.difference_between_days in range(25, 28):
            self.weekdayname = 'Седмица четвертая по Пасхе. Попраздненство Преполовения'
        elif self.difference_between_days in [28]:
            self.weekdayname = '{red}Неделя о Самаряныни.{end}'
        elif self.difference_between_days in range(29, 31):
            self.weekdayname = 'Седмица пятая по Пасхе. Попраздненство Преполовения.'
        elif self.difference_between_days in [31]:
            #TODO:Найти чин службы.
            self.weekdayname = '{red}Отдание празника Преполовения.{end}'
        elif self.difference_between_days in range(32, 35):
            self.weekdayname = 'Седмица пятая по Пасхе.'
        elif self.difference_between_days in [35]:
            self.weekdayname = '{red}Неделя о Слепом.{red}'
        elif self.difference_between_days in range(36, 38):
            self.weekdayname = 'Седмица шестая по Пасхе'
        elif self.difference_between_days in [38]:
            self.weekdayname = '{red}Отдание Пасхи (Сл.).{end}'
        elif self.difference_between_days in [39]:
            self.weekdayname = '{red}⊕ Вознесение Господне.{end}'
        elif self.difference_between_days in range(40, 42):
            self.weekdayname = 'Попраздненство Вознесения. Седмица шестая по Пасхе.'
        elif self.difference_between_days in [42]:
            self.weekdayname = '{red}Неделя свв. Отцов первого Вселенского собора.{end}'
        elif self.difference_between_days in range(43, 46):
            self.weekdayname = 'Попраздненство Вознесения. Седмица седьмая по Пасхе.'
        elif self.difference_between_days in [46]:
            self.weekdayname = '{red}Отдание праздника Вознесения (Сл.).{end}'
        elif self.difference_between_days in [47]:
            self.weekdayname = 'Седмица седьмая по Пасхе.'
        elif self.difference_between_days in [48]:
            self.weekdayname = ('В субботу седьмую по Пасхе совершаем память '
                                'всем успопшим от века во Христа верующим '
                                'отцам и братьям нашим.')
        elif self.difference_between_days in [49]:
            self.weekdayname = '{red}⊕ Пятидесятница. День святой Тройцы.{end}'
        elif self.difference_between_days in [50]:
            self.weekdayname = '{red}Понедельник святого Духа (Сл.).{end}'
        elif self.difference_between_days in range(51, 55):
            self.weekdayname = 'Седмица первая по Пятидесятнице.'
        elif self.difference_between_days in [55]:
            self.weekdayname = '{red}Отдание праздника Пятидесятницы (Сл.).{end}'
        elif self.difference_between_days in [56]:
            self.weekdayname = '{red}Неделя Всех святых.{end}'
        #Неделя свв. Отцов, устав 16 июля.
        elif self.day in [13, 14, 15, 16, 17, 18, 19] and self.month in [7] and self.weekday in [0]:
            self.weekdayname = ('%s неделя по Пятидесятнице. {red}В сию неделю память совершаем святых отец, '
                                'иже на первом соборе, в Никее сшедшася, 318. На втором соборе, сшедшася '
                                'в царствующем граде, 150. На третием соборе во Ефесе, 200. На четвертом '
                                'соборе, иже в Халкидоне, 630. На пятом соборе, 165. На шестом соборе, 170. '
                                'И всех вкупе, 1633.{end}') % str(self.week_after_pentecost)
        #Неделя по Воздвижении.
        elif self.day in [15, 16, 17, 18, 19, 20, 21] and self.month in [9] and self.weekday in [0]:
            self.weekdayname = ('{red}Неделя по Воздвижении.{end} '
                                '%s неделя по Пятидесятнице.') % str(self.week_after_pentecost)
        #Неделя свв. Отцов, устав 11 октября.
        elif self.day in [8, 9, 10, 11, 12, 13, 14] and self.month in [10] and self.weekday in [0]:
            self.weekdayname = ('%s неделя по Пятидесятнице. {red}В сию неделю память совершаем '
                                'святаго вселенскаго собора седьмаго, иже в Никеи собравшевся второе, '
                                'святых отец, 367. На потребление и посрамление безбожных предании, '
                                'хритстоненавидец и християноукоритель, и иконоборец, Копронима же '
                                'нечестиваго, и окаяных его епископ, и неосвященных его архиерей, '
                                'и того безбожнаго и окаяннаго собора.{end}') % str(self.week_after_pentecost)
        #Неделя свв. Праотец.
        elif self.day in [11, 12, 13, 14, 15, 16, 17] and self.month in [12] and self.weekday in [0]:
            self.weekdayname = ('{red}Неделя святых Праотец. '
                                '%s неделя по Пятидесятнице (Пл.).{end}') % str(self.week_after_pentecost)
        #Суббота перед Рожеством.
        elif self.day in [18, 19, 20, 21, 22, 23, 24] and self.month in [12] and self.weekday in [6]:
            self.weekdayname = ('Суббота перед Рожеством Христовым. '
                                '%s суббота по Пятидесятнице.') % str(self.week_after_pentecost + 1)
        #Неделя перед Рожеством.
        elif self.day in [18, 19, 20, 21, 22, 23, 24] and self.month in [12] and self.weekday in [0]:
            self.weekdayname = ('{red}Неделя пред Рожеством Христовым, святых Отец. '
                                '%s неделя по Пятидесятнице (Пл.).{end}') % str(self.week_after_pentecost)
        #Суббота после Рожества.
        elif self.day in [26, 27, 28, 29, 30, 31] and self.month in [12] and self.weekday in [6]:
            self.weekdayname = ('Суббота после Рожества Христова. '
                                '%s суббота по Пятидесятнице.') % str(self.week_after_pentecost + 1)
        #Неделя после Рожества.
        elif self.day in [26, 27, 28, 29, 30, 31] and self.month in [12] and self.weekday in [0]:
            self.weekdayname = ('{red}Неделя после Рожества Христова, святых Богоотец. '
                                '%s неделя по Пятидесятнице (Пл.).{end}') % str(self.week_after_pentecost)
        elif self.day in [1] and self.month in [1] and self.weekday in [0]:
            self.weekdayname = ('{red}Неделя после Рожества Христова, святых Богоотец. '
                                '%s неделя по Пятидесятнице (Пл.).{end}') % str(self.week_after_pentecost)
        #Суббота пред Просвещением. Бывает не каждый год.
        elif self.day in [1, 2, 3, 4, 5] and self.month in [1] and self.weekday in [6]:
            self.weekdayname = ('Суббота пред Просвещением. '
                                '%s суббота по Пятидесятнице.') % str(self.week_after_pentecost + 1)
        #Неделя пред Просвещением. Бывает не каждый год.
        elif self.day in [1, 2, 3, 4, 5] and self.month in [1] and self.weekday in [0]:
            self.weekdayname = ('{red}Неделя пред Просвещением. '
                                '%s неделя по Пятидесятнице (Пл.).{end}') % str(self.week_after_pentecost)
        #Суббота по Просвещении.
        elif self.day in [7, 8, 9, 10, 11, 12, 13] and self.month in [1] and self.weekday in [6]:
            self.weekdayname = ('Суббота по Просвещении. '
                                '%s суббота по Пятидесятнице.') % str(self.week_after_pentecost + 1)
        #Неделя по Просвещении.
        elif self.day in [7, 8, 9, 10, 11, 12, 13] and self.month in [1] and self.weekday in [0]:
            self.weekdayname = ('{red}Неделя по Просвещении. '
                                '%s неделя по Пятидесятнице (Пл.).{end}') % str(self.week_after_pentecost)
        else:
            #Полиелиос в неделю после отдания Воздвижения.
            if self.weekday in [0] and self.julian_date_today > ju_to_jd(5, 10, self.year):
                self.weekdayname = '{red}%s неделя по Пятидесятнице (Пл.).{end}' % str(self.week_after_pentecost)
            elif self.weekday in [0]:
                self.weekdayname = '%s неделя по Пятидесятнице.' % str(self.week_after_pentecost)
            #Димитревская суббота. Если Казанская [4], то переносится в следующую субботу [11].
            elif self.day in [11] and self.month in [10] and self.weekday in [6]:
                self.weekdayname = ('%s суббота по Пятидесятнице. Димитревская родительская суббота. '
                                    'Поминание усопших воинов '
                                    'и всех православных християн. ') % str(self.week_after_pentecost + 1)
            elif self.day in [1, 2, 3, 5, 6, 7] and self.month in [10] and self.weekday in [6]:
                self.weekdayname = ('%s суббота по Пятидесятнице. Димитревская родительская суббота. '
                                    'Поминание усопших воинов '
                                    'и всех православных християн. ') % str(self.week_after_pentecost + 1)
            elif self.weekday in [6]:
                self.weekdayname = '%s суббота по Пятидесятнице.' % str(self.week_after_pentecost + 1)
            else:
                self.weekdayname = '%s сeдмица по Пятидесятнице.' % str(self.week_after_pentecost + 1)
        
        return self.weekdayname

    def getSaint(self):
        """Get holidays and saints names for day."""

        self.out = ''
        self.out += menology[self.month][self.day]['first_saint'].strip()
        try:
            self.out += menology[self.month][self.day]['second_saint']
            self.out += menology[self.month][self.day]['oldbeliever_saint']
        except KeyError:
            pass
        return self.out

    def getFast(self):
        """Get fast for day."""

        #The Charter of fasts for all the year.
        #От Недели о мытаре и фарисее до Недели о блудном сыне.
        if self.difference_between_days in range(-70, -63):
            #Седмица сплошная, пища скоромная.
            self.fast = 7
        #От Недели о блудном сыне до Недели мясопустной.
        elif self.difference_between_days in range(-63, -56):
            if self.weekday in [0, 1, 2, 4, 6]:
                #Пища скоромная.
                if self.weekday in [0, 2, 4, 6] and self.saint in [1, 2, 3, 4, 5, 6]:
                    self.fast = 7
                #Устав о трапезе, кто понедельничает.
                elif self.weekday in [1] and self.saint in [0]:
                    self.fast = 8
                elif self.weekday in [1] and self.saint in [1, 2, 3]:
                    self.fast = 9
                elif self.weekday in [1] and self.saint in [4, 5]:
                    self.fast = 10
                elif self.weekday in [1] and self.saint in [6]:
                    self.fast = 11
            #Устав о трапезе, в среду и в пяток.
            elif self.weekday in [3, 5] and self.saint in [0]:
                self.fast = 1
            elif self.weekday in [3, 5] and self.saint in [1, 2, 3]:
                self.fast = 2
            elif self.weekday in [3, 5] and self.saint in [4, 5]:
                self.fast = 3
            elif self.weekday in [3, 5] and self.saint in [6]:
                self.fast = 5
        #От Недели мясопустной до Недели Сыропустной.
        elif self.difference_between_days in range(-56, -48):
            #Седмица сплошная, на трапезе — млеко, сыр, яйца.
            self.fast = 6
        #От Недели сыропустной до первой недели Великого поста.
        elif self.difference_between_days in range(-49, -42):
            #В первый и второй день Великого Поста.
            if self.weekday in [1, 2] and self.saint in [0, 1, 2, 3]:
                self.fast = 0
            # В первый и второй день Великого Поста
            #если полиелиос или Сретение.
            elif self.weekday in [1, 2] and self.saint in [4, 5, 6]:
                self.fast = 1
            elif self.weekday in [3, 4, 5] and self.saint in [0, 1, 2, 3]:
                self.fast = 1
            elif self.weekday in [3, 4, 5] and self.saint in [4, 5, 6]:
                self.fast = 2
            #В субботу Феодора Тирона.
            elif self.weekday in [6] and self.saint in [0, 1, 2, 3, 4, 5]:
                self.fast = 3
        #От первой недели Великого поста
        #до второй недели Великого поста.
        elif self.difference_between_days in range(-42, -35):
            #В неделю Православия.
            if self.weekday in [0] and self.saint in [0, 1, 2, 3, 4, 5]:
                self.fast = 3
            #В понедельник, среду, пятницу.
            elif self.weekday in [1, 3, 5] and self.saint in [0, 1, 2, 3]:
                self.fast = 1
            #В понедельник, среду, пятницу если полиелиос.
            elif self.weekday in [1, 3, 5] and self.saint in [4, 5]:
                self.fast = 2
            #В понедельник, среду, пятницу если Благовешение.
            elif self.weekday in [1, 3, 5] and self.saint in [6]:
                self.fast = 5
            #Во вторник и четверг.
            elif self.weekday in [2, 4] and self.saint in [0, 1, 2, 3]:
                self.fast = 2
            #Во вторник и четверг если полиелиос.
            elif self.weekday in [2, 4] and self.saint in [4, 5]:
                self.fast = 3
            #Во вторник и четверг если Благовещение.
            elif self.weekday in [2, 4] and self.saint in [6]:
                self.fast = 5
            #В субботу вторую Великого поста.
            elif self.weekday in [6] and self.saint in [0, 1, 2, 3, 4, 5]:
                self.fast = 3
            #В субботу если Благовещенье.
            elif self.weekday in [6] and self.saint in [6]:
                self.fast = 5
        #От второй недели Великого поста
        #до третьей недели Великого поста.
        elif self.difference_between_days in range(-35, -28):
            #В неделю Вторую.
            if self.weekday in [0] and self.saint in [0, 1, 2, 3, 4, 5]:
                self.fast = 3
            #В неделю если Благовещенье.
            elif self.weekday in [0] and self.saint in [6]:
                self.fast = 5
            #В понедельник, среду, пятницу.
            elif self.weekday in [1, 3, 5] and self.saint in [0, 1, 2, 3]:
                self.fast = 1
            #В понедельник, среду, пятницу если полиелиос.
            elif self.weekday in [1, 3, 5] and self.saint in [4, 5]:
                self.fast = 2
            #В понедельник, среду, пятницу если Благовешение.
            elif self.weekday in [1, 3, 5] and self.saint in [6]:
                self.fast = 5
            #Во вторник и четверг.
            elif self.weekday in [2, 4] and self.saint in [0, 1, 2, 3]:
                self.fast = 2
            #Во вторник и четверг если полиелиос.
            elif self.weekday in [2, 4] and self.saint in [4, 5]:
                self.fast = 3
            #Во вторник и четверг если Благовещение.
            elif self.weekday in [2, 4] and self.saint in [6]:
                self.fast = 5
            #В субботу третью Великого поста.
            elif self.weekday in [6] and self.saint in [0, 1, 2, 3, 4, 5]:
                self.fast = 3
            #В субботу третью если Благовещенье.
            elif self.weekday in [6] and self.saint in [6]:
                self.fast = 5
        #От третьей недели Великого поста до четвертой недели Великого поста.
        elif self.difference_between_days in range(-28, -21):
            #В неделю Крестопоклонную.
            if self.weekday in [0] and self.saint in [0, 1, 2, 3, 4, 5]:
                self.fast = 3
            #В неделю Крестопоклонную если Благовещенье.
            elif self.weekday in [0] and self.saint in [6]:
                self.fast = 5
            #В понедельник, среду, пятницу.
            elif self.weekday in [1, 3, 5] and self.saint in [0, 1, 2, 3]:
                self.fast = 1
            #В понедельник, среду, пятницу если полиелиос.
            elif self.weekday in [1, 3, 5] and self.saint in [4, 5]:
                self.fast = 2
            #В понедельник, среду, пятницу если Благовещение.
            elif self.weekday in [1, 3, 5] and self.saint in [6]:
                self.fast = 5
            #Во вторник и четверг.
            elif self.weekday in [2, 4] and self.saint in [0, 1, 2, 3]:
                self.fast = 2
            #Во вторник и четверг если полиелиос.
            elif self.weekday in [2, 4] and self.saint in [4, 5]:
                self.fast = 3
            #Во вторник и четверг если Благовещение.
            elif self.weekday in [2, 4] and self.saint in [6]:
                self.fast = 5
            #В субботу четвертую Великого поста.
            elif self.weekday in [6] and self.saint in [0, 1, 2, 3, 4, 5]:
                self.fast = 3
            #В субботу четвертую если Благовещенье.
            elif self.weekday in [6] and self.saint in [6]:
                self.fast = 5
        #От четвертой недели Великого поста до пятой недели Великого поста.
        elif self.difference_between_days in range(-21, -14):
            #В неделю Иоанна Лествичника.
            if self.weekday in [0] and self.saint in [0, 1, 2, 3, 4, 5]:
                self.fast = 3
            #В неделю Иоанна Лествичника если Благовещенье.
            elif self.weekday in [0] and self.saint in [6]:
                self.fast = 5
            #В понедельник, если Благовещение в четверг,
            #а Марьино стояние во вторник.
            elif self.weekday in [1] and self.day in [22] and self.saint in [0, 1, 2, 3]:
                self.fast = 2
            #В понедельник.
            elif self.weekday in [1] and self.saint in [1, 2, 3]:
                self.fast = 1
            #В понедельник, если полиелиос.
            elif self.weekday in [1] and self.saint in [4, 5]:
                self.fast = 2
            #В понедельник, если Благовещение.
            elif self.weekday in [1] and self.saint in [6]:
                self.fast = 5
            #Во вторник Марьино стояние, если Благовещение в четверг.
            elif self.weekday in [2] and self.day in [23] and self.saint in [0, 1, 2, 3, 4, 5]:
                self.fast = 3
            #Если 40 мученников попадают в четверг Великого канона, то он
            #переносится на вторник. Во вторник — пища с маслом.
            elif self.weekday in [2] and self.day in [7] and self.saint in [0, 1, 2, 3]:
                self.fast = 3
            #Во вторник.
            elif self.weekday in [2] and self.saint in [0, 1, 2, 3]:
                self.fast = 2
            #Во вторник если полиелиос.
            elif self.weekday in [2] and self.saint in [4, 5]:
                self.fast = 3
            #Если Благовещение во вторник.
            elif self.weekday in [2] and self.saint in [6]:
                self.fast = 5
            #В среду.
            elif self.weekday in [3] and self.saint in [0, 1, 2, 3, 4, 5]:
                self.fast = 2
            #В среду, если Благовещение.
            elif self.weekday in [3] and self.saint in [6]:
                self.fast = 5
            #В четверг, Марьино стояние.
            elif self.weekday in [4] and self.saint in [0, 1, 2, 3, 4, 5]:
                self.fast = 3
            #В четверг, если Благовещение.
            elif self.weekday in [4] and self.saint in [6]:
                self.fast = 5
            #В пятницу.
            elif self.weekday in [5] and self.saint in [0, 1, 2, 3]:
                self.fast = 1
            #В пятницу, если полиелиос.
            elif self.weekday in [5] and self.saint in [4, 5]:
                self.fast = 2
            #В пятницу если Благовещение.
            elif self.weekday in [5] and self.saint in [6]:
                self.fast = 5
            #В субботу Акафиста.
            elif self.weekday in [6] and self.saint in [0, 1, 2, 3, 4, 5]:
                self.fast = 3
            #В субботу Акафиста, если Благовещение.
            elif self.weekday in [6] and self.saint in [6]:
                self.fast = 5
        #От пятой недели Великого поста до Вербного воскресенья.
        elif self.difference_between_days in range(-14, -7):
            #В неделю  преп. Марьи Египетской.
            if self.weekday in [0] and self.saint in [0, 1, 2, 3, 4, 5]:
                self.fast = 3
            #В неделю  преп. Марьи Египетской,
            #если Благовещение.
            elif self.weekday in [0] and self.saint in [6]:
                self.fast = 5
            #В понедельник, среду, пятницу.
            elif self.weekday in [1, 3, 5] and self.saint in [0, 1, 2, 3]:
                self.fast = 1
            #В понедельник, среду, пятницу если полиелиос.
            elif self.weekday in [1, 3, 5] and self.saint in [4, 5]:
                self.fast = 2
            #В понедельник, среду, пятницу если Благовешение.
            elif self.weekday in [1, 3, 5] and self.saint in [6]:
                self.fast = 5
            #Во вторник и четверг.
            elif self.weekday in [2, 4] and self.saint in [0, 1, 2, 3]:
                self.fast = 2
            #Во вторник и четверг если полиелиос.
            elif self.weekday in [2, 4] and self.saint in [4, 5]:
                self.fast = 3
            #Во вторник и четверг если Благовещение.
            elif self.weekday in [2, 4] and self.saint in [6]:
                self.fast = 5
            #В субботу Лазаря.
            elif self.weekday in [6] and self.saint in [0, 1, 2, 3, 4, 5]:
                self.fast = 4
            #В субботу если Благовещенье.
            elif self.weekday in [6] and self.saint in [6]:
                self.fast = 5
        #Страстная седмица.
        elif self.difference_between_days in range(-7, 0):
            #В неделю Ваий.
            if self.weekday in [0] and self.saint in [0, 1, 2, 3, 4, 5, 6]:
                self.fast = 5
            #В Страстной понедельник, вторник, среду.
            elif self.weekday in [1, 2, 3] and self.saint in [0, 1, 2, 3]:
                self.fast = 1
            #В Страстной понедельник, вторник, среду,
            #если полиелиос.
            elif self.weekday in [1, 2, 3] and self.saint in [4, 5]:
                self.fast = 1
            #В Страстной понедельник,  вторник, среду,
            #если Благовещение.
            elif self.weekday in [1, 2, 3] and self.saint in [6]:
                self.fast = 3
            #В Великий четверток.
            elif self.weekday in [4] and self.saint in [0, 1, 2, 3, 4, 5]:
                self.fast = 14
            #В Великий четверток, если Благовещение.
            elif self.weekday in [4] and self.saint in [6]:
                self.fast = 3
            #В Великий пяток и Великую субботу
            #трапеза не поставляется.
            elif self.weekday in [5, 6] and self.saint in [0, 1, 2, 3, 4, 5]:
                self.fast = 0
            #В Великий пяток и Великую субботу,
            #если Благовещение.
            elif self.weekday in [5, 6] and self.saint in [6]:
                self.fast = 2
        #Светлая седмица.
        elif self.difference_between_days in range(0, 7):
                #Седмица сплошная, пища скоромная.
                self.fast = 7
        #От Недели Фоминой до Пятидесятницы.
        elif self.difference_between_days in range(7, 50):
            #Неделя Фомина и другие недели.
            if self.weekday in [0] and self.saint in [0, 1, 2, 3, 4, 5]:
                self.fast = 7
            #В для тех кто постится в понедельник.
            elif self.weekday in [1] and self.saint in [0, 1, 2, 3, 4, 5]:
                self.fast = 11
            #Во вторник, четверг, субботу.
            elif self.weekday in [2, 4, 6] and self.saint in [0, 1, 2, 3, 4, 5]:
                    self.fast = 7
            #В среду, пятницу.
            elif self.weekday in [3, 5] and self.saint in [0, 1, 2, 3, 4, 5]:
                    self.fast = 5
            #Сплошная седмица от Пятидесятницы до недели Всех святых.
            elif self.difference_between_days in range(50, 58):
                self.fast = 7
        #Петров пост.
        elif self.julian_date_today in range(self.julian_date_easter + 57, ju_to_jd(29, 6, self.year)):
            #В понедельник, среду, пятницу сухоядение,
            #если святой на 4.
            if self.weekday in [1, 3, 5] and self.saint in [0]:
                self.fast = 1
            #В понедельник, среду, пятницу
            #пища без масла, если святой на 6 или полиелеос.
            elif self.weekday in [1, 3, 5] and self.saint in [0, 1, 2, 3, 4]:
                self.fast = 2
            #В понедельник, среду, пятницу
            #пища с маслом, если бдение.
            elif self.weekday in [1, 3, 5] and self.saint in [5]:
                self.fast = 3
            #В понедельник, среду, пятницу
            #на трапезе рыба, если Рождество Иоанна Предотечи.
            elif self.weekday in [1, 3, 5] and self.saint in [6]:
                self.fast = 5
            #Во вторник, четверг, субботу, неделю,
            #на трапезе рыба.
            elif self.weekday in [0, 2, 4, 6] and self.saint in [0, 1, 2, 3, 4, 5, 6]:
                self.fast = 5
        #Мясоед от дня свв. апп. Петра и Павла до праздника происхождения Креста.
        elif self.julian_date_today in range(ju_to_jd(29, 6, self.year), ju_to_jd(1, 8, self.year)):
            #Неделя, вторник, четверг, суббота.
            if self.weekday in [0, 2, 4, 6] and self.saint in [0, 1, 2, 3, 4, 5, 6]:
                self.fast = 7
            #В для тех кто постится в понедельник.
            elif self.weekday in [1] and self.saint in [0, 1]:
                self.fast = 9
            #В для тех кто постится в понедельник,
            #когда Славословие и Полиелеос.
            elif self.weekday in [1] and self.saint in [2, 3, 4, 5]:
                self.fast = 10
            #Великобденный в понедельник.
            elif self.weekday in [1] and self.saint in [6]:
                self.fast = 11
            #Среда, пятница.
            elif self.weekday in [3, 5] and self.saint in [0, 1]:
                self.fast = 2
            #когда Славословие и Полиелеос.
            elif self.weekday in [3, 5] and self.saint in [2, 3, 4, 5]:
                self.fast = 3
            #Великобденный в среду, пятницу.
            elif self.weekday in [3, 5] and self.saint in [6]:
                self.fast = 5
        #Успенский пост.
        elif self.julian_date_today in range(ju_to_jd(1, 7, self.year), ju_to_jd(15, 8, self.year)):
            #В понедельник, среду, пятницу сухоядение,
            #если святой на 4.
            if self.weekday in [1, 3, 5] and self.saint in [0]:
                self.fast = 1
            #В понедельник, среду, пятницу
            #пища без масла, если святой на 6 или полиелеос.
            elif self.weekday in [1, 3, 5] and self.saint in [1, 2, 3, 4]:
                self.fast = 2
            #В понедельник, среду, пятницу
            #пища с маслом, если бдение.
            elif self.weekday in [1, 3, 5] and self.saint in [5]:
                self.fast = 3
            #Во вторник, четверг, субботу, неделю,
            #на трапезе масло.
            elif self.weekday in [0, 2, 4, 6] and self.saint in [0, 1, 2, 3, 4, 5]:
                self.fast = 5
            #Рыба на Преображение.
            elif self.weekday in [0, 1, 2, 3, 4, 5, 6] and self.saint in [6]:
                self.fast = 5
        #Усекновение.
        elif self.julian_date_today == ju_to_jd(29, 8, self.year):
            self.fast = 3
        #Воздвижение.
        elif self.julian_date_today == ju_to_jd(14, 9, self.year):
            self.fast = 3
        #Мясоед от праздника Успения до памяти ап. Филиппа.
        elif self.julian_date_today in range(ju_to_jd(15, 8, self.year), ju_to_jd(14, 11, self.year)):
            #Неделя, вторник, четверг, суббота.
            if self.weekday in [0, 2, 4, 6] and self.saint in [0, 1, 2, 3, 4, 5, 6]:
                self.fast = 7
            #Для тех кто постится в понедельник.
            elif self.weekday in [1] and self.saint in [0, 1]:
                self.fast = 9
            #В для тех кто постится в понедельник,
            #когда славословие и полиелеос.
            elif self.weekday in [1] and self.saint in [2, 3, 4]:
                self.fast = 10
            #Бденный, великобденный в понедельник.
            elif self.weekday in [1] and self.saint in [5, 6]:
                self.fast = 11
            #Среда, пятница.
            elif self.weekday in [3, 5] and self.saint in [0, 1]:
                self.fast = 2
            #Когда славословие и полиелеос, бдение.
            elif self.weekday in [3, 5] and self.saint in [2, 3, 4, 5]:
                self.fast = 3
            #Великобденный в среду, пятницу.
            elif self.weekday in [3, 5] and self.saint in [6]:
                self.fast = 5
        #От дня ап. Филиппа до дня свт. Николы.
        elif self.julian_date_today in range(ju_to_jd(14, 11, self.year), ju_to_jd(6, 12, self.year)):
            #В понедельник, среду, пятницу сухоядение,
            #если святой на 4.
            if self.weekday in [1, 3, 5] and self.saint in [0]:
                self.fast = 1
            #В понедельник, среду, пятницу
            #пища без масла, если святой на 6 или полиелеос.
            elif self.weekday in [1, 3, 5] and self.saint in [1, 2, 3, 4]:
                self.fast = 2
            #В понедельник, среду, пятницу
            #пища с маслом, если бдение.
            elif self.weekday in [1, 3, 5] and self.saint in [5]:
                self.fast = 3
            #Введение Пресвятой Богородицы,
            #на трапезе рыба.
            elif self.weekday in [1, 3, 5] and self.saint in [6]:
                self.fast = 5
            #Во вторник, четверг, субботу, неделю,
            #на трапезе рыба.
            elif self.weekday in [0, 2, 4, 6] and self.saint in [0, 1, 2, 3, 4, 5, 6]:
                self.fast = 5
        #Предпразднество Рожества.
        elif self.day in [20, 21, 22, 23, 24] and self.month in [12]:
            #В будние дни пища без масла.
            if self.weekday in [1, 2, 3, 4, 5] and self.saint in [0, 1, 2, 3, 4, 5]:
                self.fast = 2
            #В субботу, неделю пища с маслом.
            elif self.weekday in [0, 6] and self.saint in [0, 1, 2, 3, 4, 5]:
                self.fast = 3
        #От дня свт. Николы до Рожества.
        elif self.julian_date_today in range(ju_to_jd(6, 12, self.year), ju_to_jd(25, 12, self.year)):
            #В понедельник, среду, пятницу сухоядение,
            #если святой на 4.
            if self.weekday in [1, 3, 5] and self.saint in [0]:
                self.fast = 1
            #В понедельник, среду, пятницу
            #пища без масла, если святой на 6 или полиелеос.
            elif self.weekday in [1, 3, 5] and self.saint in [0, 1, 2, 3, 4]:
                self.fast = 2
            #В понедельник, среду, пятницу
            #пища с маслом, если бдение.
            elif self.weekday in [1, 3, 5] and self.saint in [5]:
                self.fast = 3
            #Во вторник и четверток едим с маслом.
            elif self.weekday in [2, 4] and self.saint in [0, 1, 2, 3, 4, 5]:
                self.fast = 3
            #В субботу, неделю
            #на трапезе рыба.
            elif self.weekday in [0, 6] and self.saint in [0, 1, 2, 3, 4, 5]:
                self.fast = 5
        #Навечерие Богоявления.
        elif self.julian_date_today == ju_to_jd(5, 1, self.year):
            #В будние дни пища без масла.
            if self.weekday in [1, 2, 3, 4, 5] and self.saint in [0, 1, 2, 3, 4, 5]:
                self.fast = 2
            #В субботу, неделю пища с маслом.
            elif self.weekday in [0, 6] and self.saint in [0, 1, 2, 3, 4, 5]:
                self.fast = 3
        #Святки.
        elif self.julian_date_today in range(ju_to_jd(25, 12, self.year), ju_to_jd(31, 12, self.year) + 1):
            self.fast = 7
        elif self.julian_date_today in range(ju_to_jd(1, 1, self.year), ju_to_jd(7, 1, self.year)):
            self.fast = 7
        #От Крещения Господня до Недели о мытаре и фарисее.
        else:
            #В неделю, вторник, четверг, субботу.
            if self.weekday in [0, 2, 4, 6] and self.saint in [0, 1, 2, 3, 4, 5, 6]:
                self.fast = 7
            #В для тех кто постится в понедельник.
            elif self.weekday in [1] and self.saint in [0, 1, 2, 3, 4, 5, 6]:
                self.fast = 11
            #В среду, пятницу.
            elif self.weekday in [3, 5] and self.saint in [0, 1, 2, 3, 4, 5, 6]:
                self.fast = 5

        self.fasts_word = {
            0: 'Трапеза не поставляется.',
            1: 'Сухоядение.',
            2: 'Пища без масла.',
            3: 'Пища с маслом.',
            4: 'Пища с икрой.',
            5: 'Пища с рыбой.',
            6: 'На трапезе — молоко, сыр, яйца.',
            7: 'Пища скоромная.',
            8: 'Для постящихся в понедельник — сухоядение, для остальных — пища скоромная.',
            9: 'Для постящихся в понедельник — пища без масла, для остальных — пища скоромная.',
            10: 'Для постящихся в понедельник — пища с маслом, для остальных — пища скоромная.',
            11: 'Для постящихся в понедельник — пища с рыбой,  для остальных — пища скоромная.',
            12: 'На трапезе — молоко, сыр, яйца.',
            13: 'Пища скоромная.',
            14: 'Пища без масла, пьем вино ради восопминания Вечери Господней.'
        }

        return self.fasts_word[self.fast]

    def getBow(self):
        """ Get bows for day. """

        #Устав о приходных и исходных полонах всего лета.
        #В неделю Сыропустную.
        if self.difference_between_days in [-49]:
            self.bows = ('Утром, на службе приходные и исходные поклоны  поясные, '
                         'а вечером — приходные поясные, исходные земные.')
        #Устав на полиелеосы в Великий Пост.
        elif self.difference_between_days in range(-49, 0):
            if self.weekday in [5]:
                if self.bow in [2, 3, 4, 5]:
                    self.bows = 'Приходные и исходные поклоны земные.'
                elif self.weekday in [5] and self.bow in [2, 3, 4, 5]:
                    self.bows = ('Утром, на службе приходные и исходные поклоны  земные, '
                                 'а вечером — приходные и исходные поясные.')
                #В неделю.
                elif self.weekday in [0] and self.bow in [2, 3, 4, 5]:
                    self.bows = ('Утром, на службе приходные и исходные поклоны  поясные, '
                                 'а вечером — приходные поясные, исходные земные.')
                elif self.weekday in [5] and self.bow in [2, 3, 4, 5]:
                    self.bows = ('Утром, на службе приходные и исходные поклоны  земные, '
                                 'а вечером — приходные и исходные поясные.')
                elif self.weekday in [0] and self.bow in [2, 3, 4, 5]:
                    self.bows = ('Утром, на службе приходные и исходные поклоны  поясные, '
                                 'а вечером — приходные поясные, исходные земные.')
            #В неделю.
            elif self.weekday in [0]:
                #Если нет попразненства,
                #утром, на службе приходные и
                #поклоны  поясные,
                #а вечером — приходные поясные,
                #исходные земные.
                if self.bow in [0, 1, 2, 3]:
                    self.bows = ('Утром, на службе приходные и исходные поклоны  поясные, '
                                 'а вечером — приходные поясные, исходные земные.')
            #Попраздненство: приходные
            #и исходные поясные с утра и вечером.
            elif self.bow in [5]:
                self.bows = 'Приходные и исходные поклоны поясные.'
            #В субботу поклоны поясные.
            elif self.weekday in [6]:
                #Кроме Великой  субботы.
                if self.difference_between_days in [-1]:
                    self.bows = 4
            else:
                self.bows = 'Приходные и исходные поклоны поясные.'
        #От Пасхи до недели Всех Святых.
        #поклоны поясные.
        elif self.difference_between_days in range(0, 58):
            self.bows = 'Приходные и исходные поклоны поясные.'
        #Когда нет Триоди.
        else:
            #В воскресенье.
            if self.weekday in [0]:
                self.bows = 'Приходные и исходные поклоны поясные.'
            #Среди седмицы во все двунадесятые, бденные,
            #полиелеосные праздники,
            #когда выход и славословие,
            #а также в попраздненства поклоны поясные.
            elif self.weekday in [1, 2, 3, 4]:
                #12-й праздник и попраздненство.
                if self.bow in [4, 5]:
                    self.bows = 'Приходные и исходные поклоны поясные.'
                #Бдение.
                elif self.bow in [3]:
                    self.bows = ('Утром, на службе приходные и исходные поклоны  поясные, '
                                 'а вечером — приходные поясные, исходные земные.')
                #Славословие и полиелеос.
                elif self.bow in [1, 2]:
                    self.bows = ('Утром, на службе приходные и исходные поклоны  поясные, '
                                 'а вечером — приходные и исходные земные.')
                #Когда святой на 4 или на 6,
                #и нет попразненства.
                elif self.bow in [0]:
                    self.bows = 'Приходные и исходные поклоны земные.'
            #В пятницу.
            elif self.weekday in [5]:
                #Когда святой на 4 или на 6,
                #и нет попразненства —
                #приходные земные, исходные поясные.
                if self.bow in [0]:
                    self.bows = 'Приходные поклоны земные, а исходные поклоны поясные.'
                #Бдение, полиелеос, 12-й праздник,
                #попраздненство.
                elif self.bow in [2, 3, 4, 5]:
                    self.bows = 'Приходные и исходные поклоны поясные.'
            #В субботу.
            elif self.weekday in [6]:
                self.bows = 'Приходные и исходные поклоны поясные.'

        return self.bows

    def getWeekday(self, verbose='on'):
        """Get weekday for day."""

        self.weekday_word = {
            0: 'Воскресенье',
            1: 'Понедельник',
            2: 'Вторник',
            3: 'Среда',
            4: 'Четверг',
            5: 'Пятница',
            6: 'Суббота'
        }

        if verbose == 'on':
            return self.weekday_word[weekday_ju(self.day,  self.month, self.year)]
        elif verbose == 'off':
            weekday_ju(self.day,  self.month, self.year)
        else:
            return 'Error. Value of verbose must be [on|off].'

    def getJulianDate(self, verbose='on'):
        """Get julian calendar day."""

        self.month_word = {
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

        if verbose == 'on':
            return str(self.day) + ' ' + self.month_word[self.month] + ' ' + str(self.year) + ' года по ст. ст.'
        elif verbose == 'off':
            return self.day,  self.month, self.year
        else:
            return 'Error. Value of verbose must be [on|off].'


    def getGrigorianDate(self, verbose='on'):
        """Get grigorian calendar date."""

        self.month_word = {
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

        if verbose == 'on':
            return str(self.gr_day) + ' ' + self.month_word[self.gr_month] + ' ' + str(self.gr_year) + ' года по н. ст.'
        elif verbose == 'off':
            return self.gr_day,  self.gr_month, self.gr_year
        else:
            return 'Error. Value of verbose must be [on|off].'


if __name__ == "__main__":

    import datetime
    import textwrap

    #Grigorian date today.
    gr_day = datetime.date.today().day
    gr_month = datetime.date.today().month
    gr_year = datetime.date.today().year

    cal = AncientCalendar(gr_day, gr_month, gr_year)
    print cal.getGrigorianDate(verbose='on')
    print cal.getJulianDate(verbose='on')
    print cal.getWeekday(verbose='on')
    print cal.getTone()
    print textwrap.fill(cal.getWeekdayname().format(red='\033[31m', end='\033[0m'), width=130), '\n'
    print textwrap.fill(cal.getSaint().format(red='\033[31m', end='\033[0m'), width=130)
    print cal.getFast()
    print cal.getBow()
