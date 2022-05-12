from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title_page': 'Home',
        'sub_page': 'Halaman Home',
        "nav": [
            ['/', 'Home'],
            ['blog/', 'Blog'],
            ['about/', 'About'],
        ],
        "content": 'Konten Home',
        'banner_img': 'img/banner_index.png'
    }
    return render(request, "index.html", context)
