from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, "about/index.html")


def index2(request):
    return HttpResponse("Haolo Dunia")
