from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .models import Artikel
# Create your views here.


class ArtikelListView(ListView):
    # ambil models kita mau yang manaa
    model = Artikel
    # urutkan konten berdasarkan kolom apa : default by id
    ordering = [
        'penulis_artikel'
    ]
    # mengupdate context
    extra_context = {
        'title_page': 'Blog',
        'sub_title_page': 'Halaman Blog'
    }

    # mengupdate context
    def get_context_data(self, **kwargs):
        # merge dictionary context yang sebelumnya dengan extra context
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


class BlogIndexView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = {
            'title_page': 'Blog',
            'sub_title_page': 'Halaman Blog'
        }
        return context
