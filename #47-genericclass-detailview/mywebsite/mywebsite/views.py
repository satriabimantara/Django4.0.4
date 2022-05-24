from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {
            'title_page': 'Home',
            'sub_title_page': 'Halaman Home Detail View Course'
        }
        return context
