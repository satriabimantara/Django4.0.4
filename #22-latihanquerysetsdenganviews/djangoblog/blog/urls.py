from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('artikel/', views.artikel),
    path('blog/', views.blog),
    path('jurnal/', views.jurnal),
    path('gosip/', views.gosip),
]
