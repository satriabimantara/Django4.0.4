from django.contrib import admin
from django.urls import path
from .views import artikelIndexView, addArtikelView, addArtikelView2, spesific_user_name_view

app_name = 'artikel'
urlpatterns = [
    path('specific/', spesific_user_name_view, name='specific'),
    path('tambah2/', addArtikelView2, name='tambah2'),
    path('tambah/', addArtikelView, name='tambah'),
    path('', artikelIndexView, name='index'),
]
