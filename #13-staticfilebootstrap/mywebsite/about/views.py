from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title_page': 'About',
        'sub_page': 'Halaman About',
        "nav": [
            ['/', 'Home'],
            ['/about/contact/', 'Contact'],
        ],
        "content": 'Konten About',
        'banner_img': 'img/banner_about.png',
        'app_css': '/css/about/style.css'
    }
    return render(request, "index.html", context)
