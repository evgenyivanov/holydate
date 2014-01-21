#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django import template
from django.template import Context
from django.template.loader import get_template
import datetime
from holydate import AncientCalendar
from models import Users_trace

def calendar_xml(request):

    xml = str(request.GET['xml'])

    if xml == '':
        d={'errorno':'1','text':'Tage "xml" in GET not found'}
        t = get_template("error.html")
        c = Context(d)
        html = t.render(c)
        return HttpResponse(html)
    n1 = xml.find('<date>')
    if n1 == -1:
        d={'errorno':'2','text':'Tage <date> not found'}
        t = get_template("error.html")
        c = Context(d)
        html = t.render(c)
        return HttpResponse(html)

    n2 = xml.find('</date>')
    if n2 == -1:
        d={'errorno':'3','text':'Tage </date> not found'}
        t = get_template("error.html")
        c = Context(d)
        html = t.render(c)
        return HttpResponse(html)
    if n2 - n1 <10:
        d={'errorno':'4','text':'Tags <date></date> is bad'}
        t = get_template("error.html")
        c = Context(d)
        html = t.render(c)
        return HttpResponse(html)
    date_string = xml[n1+6:n2].strip()
    if len(date_string) != 10:
        d={'errorno':'5','text':'Date format is 01/01/2000'}
        t = get_template("error.html")
        c = Context(d)
        html = t.render(c)
        return HttpResponse(html)

    gr_day = int(date_string[0:2])
    gr_month = int(date_string[4:5])
    gr_year =  int(int(date_string[7:10]))
    cal = AncientCalendar(gr_day, gr_month, gr_year)

    dayold = cal.getJulianDate()
    daynew = cal.getGrigorianDate()
    weekday = cal.getWeekday(verbose='on')
    weekname = cal.getWeekdayname()#.format(red="<span style='color:red'>", end="</span>")
    tone = cal.getTone()
    saints = cal.getSaint()#.format(red="<span style='color:red'>", end="</span>")
    food =  cal.getFast()
    bows = cal.getBow()


    d = {'dayold':dayold,'daynew':daynew,'weekday':weekday,'weekname':weekname,'tone':tone,'saints':saints,'food':food,'bows':bows,'userdate':date_string}
    #d.update({'weekcolor':weekcolor})

    t = get_template("xml.html")
    c = Context(d)
    html = t.render(c)
    return HttpResponse(html)


def test_xml(request):
    d={}
    t = get_template("test_xml.html")
    c = Context(d)
    html = t.render(c)
    return HttpResponse(html)

def body_calendar(request):

    obj = Users_trace()
    obj.date = datetime.datetime.now()
    obj.ip = str(request.META['REMOTE_ADDR'])
    obj.save()


 #Grigorian date today.
    gr_day = int(request.GET['uday'])
    gr_month = int(request.GET['umonth'])
    gr_year =  int(request.GET['uyear'])
    cal = AncientCalendar(gr_day, gr_month, gr_year)


    dayold = cal.getJulianDate()
    daynew = cal.getGrigorianDate()
    weekday = cal.getWeekday(verbose='on')
    weekname = cal.getWeekdayname().format(red="<span style='color:red'>", end="</span>")
    tone = cal.getTone()
    saints = cal.getSaint().format(red="<span style='color:red'>", end="</span>")
    food =  cal.getFast()
    bows = cal.getBow()


    d = {'dayold':dayold,'daynew':daynew,'weekday':weekday,'weekname':weekname,'tone':tone,'saints':saints,'food':food,'bows':bows}
    #d.update({'weekcolor':weekcolor})
    st = int(request.GET['uday'])
    if st < 10:
        d2 = '0'+ str(st)
    else:
        d2 = str(st)
    st = int(request.GET['umonth'])
    if st < 10:
        d3 = '0'+ str(st)
    else:
        d3 = str(st)
    userdate= str(request.GET['uyear']) + '/'+d3+'/'+d2

    d.update({'udate': userdate})



    t = get_template("info.html")
    c = Context(d)

    html = t.render(c)
    return HttpResponse(html)


def start(request):
    d={}
    t = get_template("infometr.html")
    c = Context(d)
    html = t.render(c)
    return HttpResponse(html)
