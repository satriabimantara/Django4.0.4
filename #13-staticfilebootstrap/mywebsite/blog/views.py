from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title_page': 'Blog',
        'sub_page': 'Halaman Blog',
        "nav": [
            ['/', 'Home'],
            ['/blog/news', 'News'],
            ['/blog/article', 'Article'],
        ],
        "content": 'Konten Blog',
        'banner_img': 'img/banner_blog.png',
        'app_css': '/css/blog/style.css'
    }
    return render(request, "index.html", context)
