from django.shortcuts import redirect, render
from .models import SocialMediaModel
from .forms import SocialMediaForms
from django.views import View
from django.views.generic.base import TemplateView, RedirectView

# membuat custom Mixin untuk function-function modifikasi


class SocmedSubList:
    def get_user_by_content(self, request_get):
        if len(request_get) == 0:
            social_media_list = SocialMediaModel.objects.all()
        elif request_get.__contains__('content'):
            social_media_list = SocialMediaModel.objects.filter(
                category_content=request_get['content'])
        else:
            social_media_list = SocialMediaModel.objects.none()
        return social_media_list

# Create your views here.


class SocmedListView(SocmedSubList, TemplateView):
    template_name = 'socialmedia/index.html'

    def get_context_data(self, **kwargs):
        all_social_media = self.get_user_by_content(self.request.GET)
        all_category_content = SocialMediaModel.objects.values_list(
            'category_content', flat=True).distinct()
        context = {
            'title_page': 'Social Media',
            'sub_title': 'Halaman Social Media',
            'socialmedias': all_social_media,
            'all_category_content': all_category_content
        }
        return context


class SocmedDeleteView(RedirectView):
    pattern_name = 'socmed:index'
    permanent = False
    query_string = False

    def get_redirect_url(self, *args, **kwargs):
        SocialMediaModel.objects.filter(id=kwargs['id_username']).delete()
        return super().get_redirect_url()


class SocmedFormView(View):
    template_name = 'socialmedia/tambah.html',
    socialmedia_form = SocialMediaForms()
    mode = None
    context = {}

    def get(self, request, **params):

        if self.mode == 'update':
            akun_update = SocialMediaModel.objects.get(
                id=params['id_username'])
            data = akun_update.__dict__
            self.socialmedia_form = SocialMediaForms(
                request.POST or None,
                initial=data,
                instance=akun_update
            )
        self.context = {
            'title_page': 'Social Media',
            'sub_title': 'Halaman Social Media',
            'socialmedia_form': self.socialmedia_form,
        }
        return render(request, self.template_name, self.context)

    def post(self, request, **params):
        self.socialmedia_form = SocialMediaForms(request.POST)
        # perbarui data form
        if params.__contains__('id_username'):
            akun_update = SocialMediaModel.objects.get(
                id=params['id_username'])
            self.socialmedia_form = SocialMediaForms(
                request.POST,
                instance=akun_update
            )
        if self.socialmedia_form.is_valid():
            self.socialmedia_form.save()
        else:
            self.context['socialmedia_errors'] = self.socialmedia_form.errors
        return redirect('socmed:index')
