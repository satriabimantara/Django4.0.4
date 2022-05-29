from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)
from .models import (
    Artikel,
    KategoriArtikel
)
from .forms import ArtikelForm
# Create your views here.


'''
ARTIKEL CLASS
'''


class ArtikelIndexView(TemplateView):
    template_name = 'artikel/index.html'
    extra_context = {
        'title_page': "Artikel"
    }

    def get_context_data(self, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


class ArtikelLatestPerKategoriList():
    model = Artikel

    def get_latest_artikel_each_category(self):
        # ambil semua kategori artikel yang berbeda
        kategori_list = KategoriArtikel.objects.values_list(
            'nama_kategori', flat=True).distinct()
        # looping artikel setiap kategori yang terbaru
        querysets = []
        for kategori in kategori_list:
            artikel_latest_per_kategori = Artikel.objects.filter(
                kategori__nama_kategori__iexact=kategori)
            if artikel_latest_per_kategori:
                # kalau artikel yang diretrieve ada rowsnya tidak kosong, maka ambil rows terbaru berdasarkan kolom published
                querysets.append(
                    artikel_latest_per_kategori.latest('published'))
        return querysets


class ArtikelManageView(ListView):
    model = Artikel
    template_name = 'artikel/manage.html'
    ordering = ["-published"]
    context_object_name = 'artikel_list'


class ArtikelCreateView(CreateView):
    form_class = ArtikelForm
    template_name = 'artikel/create.html'
    extra_context = {
        'title_page': 'Manage | Tambah',
        'subtitle_page': "Tambah Artikel",
        'button': {
            'button_color': 'btn-primary',
            'button_name': 'Tambah'
        }
    }
    # success_url = reverse_lazy('artikel:list 1')

    # def get_success_url(self):
    #     if not self.request.is_ajax():
    #         return reverse('artikel:detail', kwargs={'pk': self.object.id})
    #     return super().get_success_url()

    def get_context_data(self, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


class ArtikelDeleteView(DeleteView):
    model = Artikel
    template_name = 'artikel/delete_confirmation.html'
    success_url = reverse_lazy('artikel:manage')
    context_object_name = 'artikel_deleted'


class ArtikelUpdateView(UpdateView):
    model = Artikel
    template_name = 'artikel/create.html'
    form_class = ArtikelForm
    extra_context = {
        'title_page': 'Manage | Update',
        'subtitle_page': "Update Artikel",
        'button': {
            'button_color': 'btn-warning',
            'button_name': 'Update'
        }
    }

    def get_context_data(self, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


class ArtikelKategoriListView(ListView):
    model = Artikel
    template_name = 'artikel/kategori_list.html'
    ordering = ["-published"]
    context_object_name = 'artikel_list'
    paginate_by = 4

    def get_queryset(self):
        '''
        Query SQL:
        SELECT * FROM Artikel WHERE Artikel.nama_kategori=x
        '''
        artikel_per_kategori = self.model.objects.filter(
            kategori__nama_kategori__iexact=self.kwargs['nama_kategori'])
        self.queryset = artikel_per_kategori
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        kategori_list = KategoriArtikel.objects.values_list(
            'nama_kategori', flat=True).distinct().exclude(nama_kategori=self.kwargs['nama_kategori'])
        self.kwargs.update({
            'kategori_list': kategori_list,
            'title_page': "Artikel"
        })
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


class ArtikelListView(ListView):
    model = Artikel
    template_name = 'artikel/list.html'
    context_object_name = 'artikel_list'
    ordering = ['-published']
    paginate_by = 4

    def get_context_data(self, **kwargs):
        kategori_list = KategoriArtikel.objects.values_list(
            'nama_kategori', flat=True).distinct()
        self.kwargs.update({
            'kategori_list': kategori_list,
            'title_page': "Artikel"
        })
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


class ArtikelDetailView(DetailView):
    model = Artikel
    template_name = 'artikel/detail.html'
    context_object_name = 'artikel_detail'

    def get_context_data(self, **kwargs):
        self.kwargs.update({
            'title_page': "Detail Artikel"
        })
        kategori_list = KategoriArtikel.objects.values_list(
            'nama_kategori', flat=True).distinct().exclude(
                nama_kategori=self.object.kategori
        )
        self.kwargs.update({
            'kategori_list': kategori_list,
        })
        artikel_serupa = self.model.objects.filter(
            kategori__nama_kategori__iexact=self.object.kategori
        ).exclude(
            id=self.object.id
        )
        self.kwargs.update({
            'artikel_serupa': artikel_serupa,
        })
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)
