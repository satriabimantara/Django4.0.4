from django.shortcuts import render


def indexView(request):
    context = {
        'page_title': "Home"
    }
    return render(request, 'index.html', context)
