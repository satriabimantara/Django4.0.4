from django.urls import path, re_path
from . import views
app_name = "blog"
urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^post/(?P<slugInput>[\w-]+)/$',
            views.detailPostingan, name='detailPost'),
    re_path(r'^category/(?P<categoryInput>[\w-]+)/$',
            views.categoryPostingan, name='categoryPost'),
]
