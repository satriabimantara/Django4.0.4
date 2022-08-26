from django.urls import path
from .views import indexView, addView

app_name = 'blog'
urlpatterns = [
    path('add/', addView, name='add'),
    path('', indexView, name='index'),
]
