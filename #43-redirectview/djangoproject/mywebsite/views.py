from django.views.generic.base import RedirectView, TemplateView


class HomeView(RedirectView):
    # url = '/'
    pattern_name = 'index'


class HomeUserView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # jika di URL ada atribut tipe
        if self.request.GET.__contains__('tipe'):
            kwargs['tipe'] = self.request.GET['tipe']
        print(kwargs)
        return super().get_context_data(**kwargs)


class HomeRedirectView(RedirectView):
    # melempar page ke mana?
    pattern_name = 'user'

    # apakah user akan mengingat permanen perilaku ini?
    # if True then responsecode is 302, else then 301
    permanent = False

    # melekatkan query string
    query_string = True

    # mengubah nilai parameter yang dilewatkan melalui redirect view
    def get_redirect_url(self, *args, **kwargs):
        if kwargs['penulis'] == "Satria":
            kwargs['penulis'] = "satria"
        return super().get_redirect_url(*args, **kwargs)
