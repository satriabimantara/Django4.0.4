from django.contrib import admin
from django.urls import path, re_path
from .views import IndexTemplateView, ContextView, ParameterTemplateView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexTemplateView.as_view(template_name='index.html')),
    path('home/', TemplateView.as_view(template_name='home.html')),
    path('context/', ContextView.as_view()),
    re_path(r'^parameter/(?P<parameter>[0-9]+)/(?P<penulis>[\w]+)/$',
            ParameterTemplateView.as_view()),
]

'''
Catatan:
1. Jika template nya statis, maka TemplateView bisa diletakkan dan digunakan langsung dari urls.py
2. Jika templatenya tidak statis (ada context), maka TemplateView diletakkan di views.py
'''
