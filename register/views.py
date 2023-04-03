from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

def pageNotFound(request, exception):
    return redirect('mainpage/index.html')
    #HttpResponseNotFound('<h1>Страница не найдена</h1>')

# получение данных из бд
def register_start(request):
    blocks = Blocks.objects.all()
    #сделать выборкупо времени, где исключаются все блоки с датой меньше завтрашнего дня
    address = Address.object.all()
    stylist = Stylist.object.all()
    options = Option.object.all()
    return render(request, "register.html", 
    {"blocks": blocks, "address": address, "stylist": stylist, "options": options})
    
    

# Create your views here.
