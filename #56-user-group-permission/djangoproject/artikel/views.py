from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
# Create your views here.

# CARA 4 - Custom Check


@user_passes_test(lambda user: user.username == 'satria')
def spesific_user_name_view(request):
    context = {
        'title_page': request.user.username + ' Page'
    }

    return render(request, 'artikel/custom.html', context)

# CARA 3 - Lambda Decorator Check


@user_passes_test(lambda user: Group.objects.get(name='Penulis') in user.groups.all())
def addArtikelView2(request):
    context = {
        'title_page': 'Tambah Artikel Page'
    }

    return render(request, 'artikel/add_artikel.html', context)


# CARA 2 - Decorator Check
def checkIsPenulis(user):
    # ambil group untuk penulis
    group_penulis = Group.objects.get(name='Penulis')
    user_group = user.groups.all()
    status_is_penulis = group_penulis in user_group

    return status_is_penulis


@user_passes_test(checkIsPenulis)
def addArtikelView(request):
    context = {
        'title_page': 'Tambah Artikel Page'
    }

    return render(request, 'artikel/add_artikel.html', context)

# CARA 1 - Internal Check


def artikelIndexView(request):
    context = {
        'title_page': 'Artikel Page'
    }

    # ambil group untuk penulis
    group_penulis = Group.objects.get(name='Penulis')
    user_group = request.user.groups.all()

    # Buat logika untuk memisahkan view berdasarkan user group
    template_name = None
    if group_penulis in user_group:
        # logika untuk penulis
        template_name = 'artikel/index_penulis.html'
    else:
        # logika untuk selain penulis
        template_name = 'artikel/index_ex_penulis.html'

    return render(request, template_name, context)
