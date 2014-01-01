"""
All functions for orthodoxy calendar

"""


def easter(year):
    """
    Calculate orthodoxy easter 

    """

    def mod(x, y):
        return x % y

    a = mod(year, 19)
    b = mod(year, 4)
    c = mod(year, 7)
    d = mod((19 * a + 15), 30)
    e = mod((2 * b + 4 * c + 6 * d + 6), 7)

    if d + e <= 9:
        month = 3
        day = 22 + d + e
    else:
        month = 4
        day = d + e - 9

    if month == 4 and day == 26:
        day = 19

    if e == 6 and day == 28:
        day = 18

    return day, month, year


def ju_to_jd(day, month, year):
    """
    Convert julian calendar date to Julian Date(JD).

    """

    def mod(x, y):
        return x / y

    a = mod(14 - month, 12)
    b = year + 4800 - a
    c = month + 12 * a - 3
    #calculate julian date
    jd = day + mod(153 * c + 2, 5) + 365 * b + mod(b, 4) - 32083

    return jd


def gr_to_ju(day, month, year):
    """ 
    Convert Griorian calendar date to Julian Date(JD). 
    
    """

    def mod(x, y):
        return x / y

    a = mod(14 - month, 12)
    b = year + 4800 - a
    c = month + 12 * a - 3
    #calculate julian date
    jd = day + mod(153 * c + 2, 5) + 365 * b + mod(b, 4) - \
         mod(b, 100) + mod(b, 400) - 32045

    return jd


def jd_to_ju(jd):
    """ 
    Convert Julian Date(jd) to julian calendar date. 
    
    """

    def mod(x, y):
        return x / y

    e = 0
    g = jd + 32082
    f = mod(4 * g + 3, 1461)
    j = g - mod(1461 * f, 4)
    i = mod(5 * j + 2, 153)

    day = j - mod(153 * i + 2, 5) + 1
    month = i + 3 - 12 * mod(i, 10)
    year = 100 * e + f - 4800 + mod(i, 10)

    #return julian calendar date:    
    return day, month, year


def jd_to_gr(JD):
    """ 
    Convert Julian Date(JD) to Grigorian calendar date. 
    
    """

    def mod(x, y):
        return x / y

    d = JD + 32044
    e = mod(4 * d + 3, 146097)
    g = d - mod(146097 * e, 4)
    f = mod(4 * g + 3, 1461)
    j = g - mod(1461 * f, 4)
    i = mod(5 * j + 2, 153)

    day = j - mod(153 * i + 2, 5) + 1
    month = i + 3 - 12 * mod(i, 10)
    year = 100 * e + f - 4800 + mod(i, 10)

    #return Grigorian calendar date:
    return day, month, year


def weekday_ju(day, month, year):
    """ 
    Return weekday in Julian calendar(0-6 ~ Sun-Sut) 
    for year, month (1-12),  day (1-31).
       
    """

    def mod(x, y):
        return x / y

    a = mod(14 - month, 12)
    y = year - a
    m = month + (12 * a - 2)
    weekday = (5 + day + y + mod(y, 4) + mod(31 * m, 12)) % 7

    #return weekday:
    return weekday


def gr_to_jd(day, month, year):
    """ 
    Convert Griorian calendar date to Julian 
    calendar date. 
    
    """

    def mod(x, y):
        return x / y

    a = mod(14 - month, 12)
    b = year + 4800 - a
    c = month + 12 * a - 3
    #calculate JD
    jd = day + mod(153 * c + 2, 5) + 365 * b + mod(b, 4) - \
         mod(b, 100) + mod(b, 400) - 32045

    #Calculate julian calendar date from JD.
    e = 0
    g = jd + 32082
    f = mod(4 * g + 3, 1461)
    j = g - mod(1461 * f, 4)
    i = mod(5 * j + 2, 153)

    day = j - mod(153 * i + 2, 5) + 1
    month = i + 3 - 12 * mod(i, 10)
    year = 100 * e + f - 4800 + mod(i, 10)

    #return julian calendar date:    
    return day, month, year    
                    











                
