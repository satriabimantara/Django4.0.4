from django.shortcuts import render


def index(request):
    context = {
        'title_page': 'Home',
        'sub_title': 'Halaman Home'
    }
    return render(request, 'index.html', context)
