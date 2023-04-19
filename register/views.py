from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *
from datetime import datetime, timedelta
#from mainpage.models import Galery
def add_schedule():
    stylists = Stylist.objects.all()
    for worker in stylists:
        date = WorkSchedule.objects.filter(stylist = worker.pk).order_by('-day_of_work').first().day_of_work
        date = date - timedelta(days=1)
        q = WorkSchedule.objects.filter(stylist = worker.pk).filter(day_of_work__gte = date)
        if q[1].is_work == q[0].is_work == True:
            new_work_schedule = WorkSchedule(stylist = Stylist(id = worker.pk),
                day_of_work = q[1].day_of_work + timedelta(days=1), is_work = False)
        elif q[1].is_work == q[0].is_work == False:
            new_work_schedule = WorkSchedule(stylist = Stylist(id = worker.pk),
                day_of_work = q[1].day_of_work + timedelta(days=1), is_work = True)
        else:
            new_work_schedule = WorkSchedule(stylist = Stylist(id = worker.pk),
                day_of_work = q[1].day_of_work + timedelta(days=1), is_work = q[1].is_work)

        new_work_schedule.save()


def pageNotFound(request, exception):
    return redirect('')
    #HttpResponseNotFound('<h1>Страница не найдена</h1>')

# получение данных из бд
def register_start(request):
    #blocks = Blocks.objects.all()
    #сделать выборкупо времени, где исключаются все блоки с датой меньше завтрашнего дня
    #address = Address.object.all()
    #stylist = Stylist.object.all()
    #options = Option.object.all()
    #return render(request, "register.html",
    #{"blocks": blocks, "address": address, "stylist": stylist, "options": options})
    str = ""
    if request.method == 'POST':
        add_schedule()
        str = request.POST.get("test")
    return render(request, "register.html",{"str":str})

# Create your views here.
