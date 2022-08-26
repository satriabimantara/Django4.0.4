from django.contrib import admin
from django.urls import path, include
from .views import indexView


urlpatterns = [
    path('', indexView, name='index'),
    path('blog/', include("blog.urls", namespace='blog')),
    path('admin/', admin.site.urls),
]
