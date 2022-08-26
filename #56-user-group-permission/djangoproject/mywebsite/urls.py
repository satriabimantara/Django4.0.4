from django.contrib import admin
from django.urls import path, include
from .views import index, IndexView, loginView, logoutView


urlpatterns = [
    path('artikel/', include('artikel.urls', namespace='artikel')),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
    path('', IndexView.as_view(), name='index'),
    # path('', index, name='index'),
    path('admin/', admin.site.urls),
]
