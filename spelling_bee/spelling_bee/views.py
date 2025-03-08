from django.http import HttpResponse 
from django.template import loader
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def game_mode(request):
    return render(request, 'game_mode.html')

def login(request):
    return render(request, 'login.html')

def practice(request):
    return render(request, 'practice.html')

def practice_lists(request):
    return render(request, 'practice_lists.html')








