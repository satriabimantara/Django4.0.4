from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title_page': 'Halaman Blog',
        'sub_page': "Halo Dunia Blog"
    }
    return render(request, "blog/index.html", context)
