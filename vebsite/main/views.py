from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h4>Hello Django</h4>')

def about(request):
    return HttpResponse('<h4>About</h4>')

def advertising(request):
    return HttpResponse('<h2>your ad can be here</h2>')
