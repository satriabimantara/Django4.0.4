from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title_page': 'Halaman About',
        'sub_page': "Halo Dunia About"
    }
    return render(request, "about/index.html", context)
