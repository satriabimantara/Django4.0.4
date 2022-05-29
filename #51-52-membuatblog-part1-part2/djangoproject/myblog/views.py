from django.views.generic import (
    TemplateView
)
from artikel.views import ArtikelLatestPerKategoriList


class BlogHomeIndex(TemplateView, ArtikelLatestPerKategoriList):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        querysets = self.get_latest_artikel_each_category()
        extra_context = {
            'title_page': "Home",
            'artikel_latest_list': querysets
        }
        self.kwargs.update(extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)
