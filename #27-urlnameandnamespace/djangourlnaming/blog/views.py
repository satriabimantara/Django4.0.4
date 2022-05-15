from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title_page': "Blog",
        'sub_title': "Halaman Blog"
    }
    return render(request, 'blog/index.html', context)


def khusus(request, input):
    context = {
        'title_page': "Blog Khusus",
        'sub_title': "Halaman Blog Khusus " + input
    }
    return render(request, 'blog/index.html', context)


def categoryPost(request):
    context = {
        'title_page': "Blog Category",
        'sub_title': "Halaman Blog Category"
    }
    return render(request, 'blog/index.html', context)


def singlePost(request):
    context = {
        'title_page': "Blog Single Post",
        'sub_title': "Halaman Blog Single Post"
    }
    return render(request, 'blog/index.html', context)
