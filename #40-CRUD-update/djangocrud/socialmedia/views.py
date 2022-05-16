from django.shortcuts import redirect, render
from .models import SocialMediaModel
from .forms import SocialMediaForms
# Create your views here.


def index(request):
    all_social_media = SocialMediaModel.objects.all()
    context = {
        'title_page': 'Social Media',
        'sub_title': 'Halaman Social Media',
        'socialmedias': all_social_media
    }
    return render(request, 'socialmedia/index.html', context)


def update(request, id_username):
    akun_update = SocialMediaModel.objects.get(id=id_username)
    data = {
        'first_name': akun_update.first_name,
        'last_name': akun_update.last_name,
        'username': akun_update.username,
    }
    '''
    initial--> mengisi field dengan data yang diretrieve SQL
    instance--> mengupdate data sesuai dengan id data yang diretrieve
    '''
    socialmedia_form = SocialMediaForms(
        request.POST or None,
        initial=data,
        instance=akun_update
    )
    context = {
        'title_page': 'Social Media',
        'sub_title': 'Halaman Social Media',
        'socialmedia_form': socialmedia_form,
    }
    if request.method == "POST":
        if socialmedia_form.is_valid():
            socialmedia_form.save()
        else:
            context['socialmedia_errors'] = socialmedia_form.errors
        return redirect('socmed:index')
    return render(request, 'socialmedia/tambah.html', context)


def hapus(request, id_username):
    SocialMediaModel.objects.filter(id=id_username).delete()
    return redirect('socmed:index')


def tambah(request):
    socialmedia_form = SocialMediaForms(request.POST or None)
    context = {
        'title_page': 'Social Media',
        'sub_title': 'Halaman Social Media',
        'socialmedia_form': socialmedia_form,
    }
    if request.method == "POST":
        if socialmedia_form.is_valid():
            socialmedia_form.save()
        else:
            context['socialmedia_errors'] = socialmedia_form.errors
        return redirect('socmed:index')
    return render(request, 'socialmedia/tambah.html', context)
