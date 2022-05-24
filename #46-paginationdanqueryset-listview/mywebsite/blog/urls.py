from django.urls import path, re_path
from . import views

app_name = 'blog'
urlpatterns = [
    re_path(r'^(?P<penulis>\w+)/(?P<page>\d+)/$',
            views.ArtikelListView.as_view(), name='list'),
    re_path(r'^(?P<penulis>\w+)/$',
            views.ArtikelListView.as_view(), name='list'),
    path('', views.BlogIndexView.as_view(), name='index')
]
