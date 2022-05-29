from django.urls import path, re_path
from .views import (
    ArtikelIndexView,
    ArtikelListView,
    ArtikelDetailView,
    ArtikelKategoriListView,
    ArtikelCreateView,
    ArtikelManageView,
    ArtikelDeleteView,
    ArtikelUpdateView
)
app_name = 'artikel'
urlpatterns = [
    path('manage/update/<int:pk>/', ArtikelUpdateView.as_view(), name='update'),
    path('manage/delete/<int:pk>/', ArtikelDeleteView.as_view(), name='hapus'),
    path('manage/', ArtikelManageView.as_view(), name='manage'),
    path('create/', ArtikelCreateView.as_view(), name='tambah'),
    re_path(r'^kategori/(?P<nama_kategori>[\w]+)/(?P<page>\d+)$',
            ArtikelKategoriListView.as_view(), name='kategori'),
    path('list/<int:page>', ArtikelListView.as_view(), name='list'),
    path('detail/<int:pk>', ArtikelDetailView.as_view(), name='detail'),
    path('', ArtikelIndexView.as_view(), name='index'),
]
