from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def index(request):
    tasks = Task.objects.order_by('-id')  # [:1]срез, а - сортирует от последней записи до первой
    # tasks = Task.objects.order_by('title')  # сортирует по опред. полю
    # tasks = Task.objects.all() вывод всей информации
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks,
                                               'decision': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    return render(request, 'main/create.html')


def advertising(request):
    return render(request, 'main/advertising.html')


def alternative(request):
    return render(request, 'main/alternative.html')
