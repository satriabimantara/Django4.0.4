from django.contrib import admin
from django.urls import path, include
from .views import BlogHomeIndex

urlpatterns = [
    path('admin/', admin.site.urls),
    path('artikel/', include('artikel.urls', namespace='artikel')),
    path('', BlogHomeIndex.as_view(), name='index')
]
