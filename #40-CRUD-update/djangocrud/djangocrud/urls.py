from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('socialmedia/', include('socialmedia.urls', namespace='socmed')),
    path('', views.index, name='index')
]
