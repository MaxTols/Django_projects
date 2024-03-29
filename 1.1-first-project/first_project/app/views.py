import os
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, reverse


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
    current_time = datetime.now()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    path = '.'
    rez = sorted(os.listdir(path))
    msg = f"Список файлов в рабочей директории: {rez}"
    return HttpResponse(msg)


def hello_view(request):
    return render(request, 'app/hello.html')
    # name = request.GET.get('name')
    # age = int(request.GET.get('age', 20))
    # print(age)
    # return HttpResponse(f'hello, {name}')


def sum_view(request, a, b):
    result = a + b
    return HttpResponse(result)
