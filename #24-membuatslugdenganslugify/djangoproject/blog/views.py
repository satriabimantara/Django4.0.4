from http.client import HTTP_PORT
from django.http import HttpResponse
from .models import Post
# Create your views here.


def index(request):
    string = "<h1>Hello World</h1>"
    return HttpResponse(string)


def categoryPost(request, **kwargs):
    filterPost = Post.objects.filter(
        category__iexact=kwargs['categoryInput'])
    string = "<h1>Hello World</h1>" + kwargs['categoryInput']
    return HttpResponse(filterPost)


def singlePost(request, slugInput):
    # slug sudah pasti unik antar 1 baris dengan baris lainnya, sehingga gunakan get
    post = Post.objects.get(slug__iexact=slugInput)
    judul = "<h1>{}</h1>".format(post.judul)
    category = "<h2>{}</h2>".format(post.category)
    body = "<p>{}</p>".format(post.body)
    return HttpResponse(judul + category + body)
