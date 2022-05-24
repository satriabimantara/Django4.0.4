from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='func_index'),
    path('class_views', views.IndexClassView.as_view(
        template_name='index.html'), name='class_index'),
    path('class_views2', views.IndexClassView.as_view(
        template_name='index2.html'), name='class_index2'),
]
