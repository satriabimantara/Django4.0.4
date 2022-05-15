from django.urls import path, re_path
from . import views


# URL Naming and Namespacing
app_name = "blog"
urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^khusus/(?P<input>[\w-]+)/$', views.khusus, name='khusus'),
    path('category/', views.categoryPost, name='category'),
    path('single/', views.singlePost, name='single'),
]
