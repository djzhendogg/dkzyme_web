from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/base.html', {'title': "Home"})


def about(request):
    return render(request, 'main/undex.html')
