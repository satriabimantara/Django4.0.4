from django.shortcuts import render
from .models import Post

# Create your views here.


def index(request):
    # querysets dari model
    posts = Post.objects.all()
    context = {
        'title': "Blog",
        "sub_title": "Selamat datang di halaman blog",
        "posts": posts
    }
    return render(request, 'blog/index.html', context)
