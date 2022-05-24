from django.shortcuts import render
from django.views import View


'''
Functional Based Views
'''


def index(request):
    context = {
        'title_page': "Home",
        'sub_title': "Halaman Home",
    }
    if request.method == "POST":
        context['content'] = 'POST dari Functional View'
    return render(request, 'index.html', context)


'''
Class Based Views
'''


class IndexClassView(View):
    template_name = ''
    context = {
        'title_page': "Home",
        'sub_title': "Halaman Home"
    }
    # override method get dari class View

    def get(self, request, **params):
        self.context['content'] = 'GET dari Class View'
        return render(request, self.template_name, self.context)

    # override method post dari class View
    def post(self, request):
        self.context['content'] = 'POST dari Class View'
        return render(request, self.template_name, self.context)
