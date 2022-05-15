from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': "Home",
        "sub_title": "Selamat datang di halaman home",
    }
    return render(request, 'index.html', context)
