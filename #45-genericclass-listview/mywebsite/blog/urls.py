from django.urls import path
from django.views.generic import ListView
from .models import Artikel
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.BlogIndexView.as_view(), name='index'),
    path('artikel/', ListView.as_view(model=Artikel), name='artikel1'),
    path('artikel2/', views.ArtikelListView.as_view(model=Artikel), name='artikel2')
]
