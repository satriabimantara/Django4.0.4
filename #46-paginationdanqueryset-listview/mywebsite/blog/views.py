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
    # Mau ditampilkan berapa item per halaman?
    paginate_by = 2
    # mengupdate context
    extra_context = {
        'title_page': 'Blog',
        'sub_title_page': 'Halaman Blog'
    }

    # memodifikasi queryset dengan mengambil baris tertentu dari db
    def get_queryset(self):
        if self.kwargs['penulis'] != 'all':
            self.queryset = self.model.objects.filter(
                penulis_artikel__iexact=self.kwargs['penulis'])
            self.kwargs.update({
                'penulis': self.kwargs['penulis']
            })
        return super().get_queryset()

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
