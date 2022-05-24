from django.views.generic.base import TemplateView

'''
Template View
- Merupakan inheritance dari TemplateResponseMixin
- inheritance dari ContextMixin
- inheritance dari View
'''


class ParameterTemplateView(TemplateView):
    template_name = 'parameter.html'

    def get_context_data(self, **params):
        # context = params
        # save way
        context = super().get_context_data(**params)
        return context


class IndexTemplateView(TemplateView):
    pass


class ContextView(TemplateView):
    template_name = 'context.html'

    # mengambil data context
    def get_context_data(self):
        context = {
            'penulis': "Mario Teguh"
        }
        return context
