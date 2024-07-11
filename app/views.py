from django.http import HttpResponse
from django.shortcuts import render, reverse

import os
import datetime


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    path = "C:\\Users\Алина\Desktop\ProektsPY\myStartDjango"
    files = os.listdir(path)
    result = "<br>".join(files)
    return HttpResponse(result)