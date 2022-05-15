from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title_page': "Home",
        'sub_title_page': "Home Page"
    }
    return render(request, "index.html", context)
