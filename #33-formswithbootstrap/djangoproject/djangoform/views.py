from django.shortcuts import render
from .forms import FormField


def index(request):
    form_field = FormField()
    context = {
        'title_page': "Home",
        'sub_title': "Halaman Home",
        'form_field': form_field
    }

    return render(request, 'index.html', context)
