from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import PostForm
from .models import PostModel
# Create your views here.


def index(request):
    post_data = PostModel.objects.all()
    context = {
        'title_page': "Blog",
        'sub_title': "Halaman Blog",
        'post_data': post_data
    }
    return render(request, 'blog/index.html', context)


def create(request):
    post_form = PostForm()
    context = {
        'title_page': "Blog Create",
        'sub_title': "Halaman Blog Create",
        'post_form': post_form
    }
    if request.method == "POST":
        PostModel.objects.create(
            judul=request.POST['judul'],
            body=request.POST['body'],
            category=request.POST['category']
        )
        # redirect ke page ke tertentu
        return HttpResponseRedirect("/blog/")
    return render(request, 'blog/create.html', context)
