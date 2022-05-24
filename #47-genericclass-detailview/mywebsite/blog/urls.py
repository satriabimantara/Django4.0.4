from django.urls import path, re_path
from django.views.generic import DetailView
from . import views
from .models import Artikel

app_name = 'blog'
urlpatterns = [
    re_path(r'^(?P<penulis>\w+)/(?P<page>\d+)/$',
            views.ArtikelListView.as_view(), name='list'),
    re_path(r'^(?P<penulis>\w+)/$',
            views.ArtikelListView.as_view(), name='list'),
    re_path(r'^detail/(?P<slug>[\w-]+)/$',
            views.ArtikelDetailView.as_view(), name='detail'),
    #     re_path(r'^detail/(?P<slug>[\w-]+)/$',
    #             DetailView.as_view(model=Artikel), name='detail'),
    path('', views.BlogIndexView.as_view(), name='index'),
]


'''
Detail View:
1. Wajib mengirim parameter slug pada urlnya
2. Wajib membuat <nama_model>_detail.html pada templatenya
'''
