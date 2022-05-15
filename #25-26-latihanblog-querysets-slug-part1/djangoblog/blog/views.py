from django.shortcuts import render
from .models import Post
# Create your views here.


def index(request):
    allPost = Post.objects.all()
    # ambil semua nilai 'category' yang unik
    categoriesValues = Post.objects.values('category').distinct()
    context = {
        'title_page': "Blog",
        'sub_title_page': "Blog Page",
        'Posts': allPost,
        'categories': categoriesValues
    }
    return render(request, "blog/index.html", context)


def categoryPostingan(request, **kwargs):
    categoryPosts = Post.objects.filter(
        category__iexact=kwargs['categoryInput'])
    # ambil semua nilai 'category' yang unik
    categoriesValues = Post.objects.values('category').distinct()
    context = {
        'title_page': "Blog",
        'sub_title_page': "Blog Page Category "+str(kwargs['categoryInput']).capitalize(),
        'Posts': categoryPosts,
        'categories': categoriesValues
    }
    return render(request, "blog/index.html", context)


def detailPostingan(request, **kwargs):
    post_detail = Post.objects.get(slug=kwargs['slugInput'])
    context = {
        'title_page': "Blog",
        'sub_title_page': "Blog Page",
        'postingan': post_detail
    }
    return render(request, "blog/detailpostingan.html", context)
