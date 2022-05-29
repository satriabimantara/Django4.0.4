from django.urls import path, re_path
from .views import (
    ArtikelListView,
    ArtikelDetailView,
    ArtikelFormView,
    ArtikelCreateView,
    ArtikelCreateView2,
    ArtikelUpdateView,
    ArtikelUpdateView2,
    ArtikelDeleteView,
    ArtikelDeleteView2,

)
from django.views.generic import RedirectView

app_name = 'blog'
urlpatterns = [
    path('delete2/<int:pk>',
         ArtikelDeleteView2.as_view(), name='delete2'),
    path('delete/<int:pk>',
         ArtikelDeleteView.as_view(), name='delete'),
    path('update2/<int:pk>',
         ArtikelUpdateView2.as_view(), name='update2'),
    path('update/<int:pk>',
         ArtikelUpdateView.as_view(), name='update'),
    path('create', ArtikelCreateView2.as_view(), name='create'),
    #     path('create', ArtikelCreateView.as_view(), name='create'),
    #     path("create/", ArtikelFormView.as_view(), name="create"),
    re_path(r'^(?P<penulis>\w+)/(?P<page>\d+)/$',
            ArtikelListView.as_view(), name='list'),
    re_path(r'^(?P<penulis>\w+)/$',
            ArtikelListView.as_view(), name='list'),
    re_path(r'^detail/(?P<slug>[\w-]+)/$',
            ArtikelDetailView.as_view(), name='detail'),
    #     re_path(r'^detail/(?P<slug>[\w-]+)/$',
    #             DetailView.as_view(model=Artikel), name='detail'),
    path('', RedirectView.as_view(url='/blog/all'), name='index'),
]


'''
Detail View:
1. Wajib mengirim parameter slug pada urlnya
2. Wajib membuat <nama_model>_detail.html pada templatenya
'''
