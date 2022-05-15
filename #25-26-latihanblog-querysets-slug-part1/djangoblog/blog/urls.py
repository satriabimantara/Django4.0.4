from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    re_path(r'^post/(?P<slugInput>[\w-]+)/$', views.detailPostingan),
    re_path(r'^category/(?P<categoryInput>[\w-]+)/$', views.categoryPostingan),
]
