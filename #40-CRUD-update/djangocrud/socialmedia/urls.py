from django.urls import path, re_path
from . import views

app_name = 'socmed'
urlpatterns = [
    path('', views.index, name='index'),
    path('tambah/', views.tambah, name='tambah'),
    re_path(r'^hapus/(?P<id_username>[0-9]+)/$', views.hapus, name='hapus'),
    re_path(r'^update/(?P<id_username>[0-9]+)/$', views.update, name='update'),
]
