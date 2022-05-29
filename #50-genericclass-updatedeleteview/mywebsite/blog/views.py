from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import (
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Artikel
from .forms import ArtikelForms
# Create your views here.


class ArtikelDeleteView2(DeleteView):
    model = Artikel
    template_name = 'blog/konfirmasi_hapus.html'
    success_url = reverse_lazy('blog:list', kwargs={
        'penulis': 'all'
    })


class ArtikelDeleteView(DeleteView):
    model = Artikel
    success_url = reverse_lazy('blog:list', kwargs={
        'penulis': 'all'
    })


class ArtikelUpdateView2(UpdateView):
    model = Artikel
    # Menyeleksi atribut mana saja yang bisa diupdate
    fields = [
        'isi_artikel'
    ]


class ArtikelUpdateView(UpdateView):
    form_class = ArtikelForms
    model = Artikel
    template_name = 'blog/create.html'
    extra_context = {
        'title_page': 'Update Artikel',
        'sub_title_page': 'Halaman Update Artikel dari Update View'
    }

    def get_context_data(self, **kwargs):
        # merge dictionary context yang sebelumnya dengan extra context
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


class ArtikelCreateView2(CreateView):
    # sediakan template bernama <model>_form.html
    model = Artikel
    fields = [
        'judul_artikel',
        'isi_artikel',
        'penulis_artikel'
    ]
    extra_context = {
        'title_page': 'Tambah Artikel',
        'sub_title_page': 'Halaman Tambah Artikel dari Create View 2'
    }

    def get_context_data(self, **kwargs):
        # merge dictionary context yang sebelumnya dengan extra context
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


class ArtikelCreateView(CreateView):
    # bisa menggunakan form asalkan inherit dari ModelForm
    form_class = ArtikelForms
    template_name = 'blog/create.html'

    # success urlnya ada pada method get_absolute_url pada Artikel model, sehingga pada bagian ini tidak ada success url

    extra_context = {
        'title_page': 'Tambah Artikel',
        'sub_title_page': 'Halaman Tambah Artikel dari Create View'
    }

    def get_context_data(self, **kwargs):
        # merge dictionary context yang sebelumnya dengan extra context
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


class ArtikelFormView(FormView):
    template_name = 'blog/create.html'
    form_class = ArtikelForms
    # success_url = '/blog/all/'
    success_url = reverse_lazy(
        'blog:list',
        kwargs={
            'penulis': 'all'
        }
    )
    extra_context = {
        'title_page': 'Tambah Artikel',
        'sub_title_page': 'Halaman Tambah Artikel'
    }

    # menyimpan data yang sudah dilempar dari form
    def form_valid(self, form):
        # print(form.cleaned_data)
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # merge dictionary context yang sebelumnya dengan extra context
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


class ArtikelDetailView(DetailView):
    model = Artikel
    extra_context = {
        'title_page': 'Blog Detail',
        'sub_title_page': 'Halaman Blog Detail'
    }

    def get_context_data(self, **kwargs):
        # mengambil artikel lain selain yang sudah diambil ini
        another_articles = self.model.objects.exclude(slug=self.kwargs['slug'])
        self.kwargs.update(self.extra_context)
        self.kwargs.update({
            'another_articles': another_articles
        })
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


class ArtikelListView(ListView):
    # ambil models kita mau yang manaa
    model = Artikel
    # urutkan konten berdasarkan kolom apa : default by id
    ordering = [
        'publish_artikel'
    ]
    # Mau ditampilkan berapa item per halaman?
    # paginate_by = 2
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
