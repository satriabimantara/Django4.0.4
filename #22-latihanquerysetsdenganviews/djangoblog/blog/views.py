from django.shortcuts import render
from .models import Post
# Create your views here.


def index(request):
    allPost = Post.objects.all()
    context = {
        'title': "Blog",
        "sub_title": "Selamat datang di halaman blog",
        'allPost': allPost
    }
    return render(request, 'blog/index.html', context)


def artikel(request):
    allPost = Post.objects.filter(category__iexact="artikel")
    context = {
        'title': "Blog",
        "sub_title": "Selamat datang di halaman blog/artikel",
        'allPost': allPost
    }
    return render(request, 'blog/index.html', context)


def jurnal(request):
    allPost = Post.objects.filter(category__iexact="jurnal")
    context = {
        'title': "Blog",
        "sub_title": "Selamat datang di halaman blog/jurnal",
        'allPost': allPost
    }
    return render(request, 'blog/index.html', context)


def blog(request):
    allPost = Post.objects.filter(category__iexact="blog")
    context = {
        'title': "Blog",
        "sub_title": "Selamat datang di halaman blog/blog",
        'allPost': allPost
    }
    return render(request, 'blog/index.html', context)


def gosip(request):
    allPost = Post.objects.filter(category__iexact="gosip")
    context = {
        'title': "Blog",
        "sub_title": "Selamat datang di halaman blog/gosip",
        'allPost': allPost
    }
    return render(request, 'blog/index.html', context)
