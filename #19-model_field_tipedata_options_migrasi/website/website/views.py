from django.shortcuts import render


def index(request):
    # querysets dari model
    # posts = Post.objects.all()
    context = {
        'title': "Home",
        "sub_title": "Selamat datang di halaman Home",
        # "posts": posts
    }
    return render(request, 'index.html', context)
