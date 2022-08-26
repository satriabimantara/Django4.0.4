from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        self.kwargs.update({
            'title_page': 'Home'
        })
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


def loginView(request):
    context = {
        'title_page': 'Home'
    }

    # permission check untuk mengecek apakah user sudah login
    if request.method == "GET":
        if request.user.is_authenticated:
            # logika untuk user yang sudah login
            return redirect('index')
        else:
            # redirect user ke halaman login (belum login)
            return render(request, 'login.html', context)

    if request.method == "POST":
        # mengambil data user dari form login
        username_input = request.POST['username']
        password_input = request.POST['password']

        # authenticate untuk memastikan apakah user ini ada di dalam db atau tidak
        user = authenticate(
            request,
            username=username_input,
            password=password_input
        )
        if user is not None:
            # masukan data user ke dalam request
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')

# login diperlukan untuk mengakses method logout


@login_required()
def logoutView(request):
    context = {
        'title_page': 'Logout'
    }
    if request.method == "POST":
        if request.POST['logout'] == "Submit":
            logout(request)
            return redirect('index')
    return render(request, 'logout.html', context)


def index(request):
    context = {
        'title_page': 'Home'
    }
    return render(request, 'index.html', context)
