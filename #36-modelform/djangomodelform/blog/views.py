from django.shortcuts import render, redirect
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
    post_form = PostForm(request.POST or None)
    context = {
        'title_page': "Blog Create",
        'sub_title': "Halaman Blog Create",
        'post_form': post_form,
        'post_errors': None
    }
    if request.method == "POST":
        # validasi data dari form sebelum dimasukkan ke db
        if post_form.is_valid():
            '''
            cara modelform
            '''
            post_form.save()
            '''
            cara konvensional
            '''
            # simpan data yang sudah dibersihkan
            # PostModel.objects.create(
            #     judul=post_form.cleaned_data.get('judul'),
            #     body=post_form.cleaned_data.get('body'),
            #     category=post_form.cleaned_data.get('category'),
            # )
            return redirect('blog:index')
        else:
            context['post_errors'] = post_form.errors
            print(context['post_errors'])

    return render(request, 'blog/create.html', context)
