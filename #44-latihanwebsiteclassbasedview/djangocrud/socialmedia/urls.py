from django.urls import path, re_path
from .views import (
    SocmedListView,
    SocmedFormView,
    SocmedDeleteView,
)

app_name = 'socmed'
urlpatterns = [
    path('', SocmedListView.as_view(), name='index'),
    path('tambah/', SocmedFormView.as_view(mode='tambah'), name='tambah'),
    re_path(r'^hapus/(?P<id_username>[0-9]+)/$',
            SocmedDeleteView.as_view(), name='hapus'),
    re_path(r'^update/(?P<id_username>[0-9]+)/$',
            SocmedFormView.as_view(mode='update'), name='update'),
]
