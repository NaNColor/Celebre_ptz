from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import Galery
def index(request):
    data = Galery.objects.all()
    return render(request,'index.html',{'data': data})
    #HttpResponse("MAIN")
    

def pageNotFound(request, exception):
    return redirect('mainpage/index.html')
    #HttpResponseNotFound('<h1>Страница не найдена</h1>')