"""
Halaman UI Project Views
"""
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h3>Halo Pengenalan Views</h3>")


def admin(request):
    return HttpResponse("Halo Admin")
