from django.shortcuts import render


def index(request):
    context = {
        'title_page': "Home",
        'sub_title': "Halaman Home"
    }
    if request.method == "POST":
        context['nama'] = request.POST['nama']
    return render(request, 'index.html', context)
