from django.http import HttpResponse


def index(request):
    string = "<h1>Hello World</h1>"
    return HttpResponse(string)


def angka(request, input):
    string = "<h1>Page Angka</h1>" + input
    print(input)
    return HttpResponse(string)


def tanggal(request, **kwargs):
    string = "<h1>Page Tanggal</h1>"
    tahun = kwargs['tahun']
    bulan = kwargs['bulan']
    hari = kwargs['hari']
    data_tanggal = "{}/{}/{}".format(tahun, bulan, hari)
    return HttpResponse(string+data_tanggal)


def link(request, **kwargs):
    url = kwargs['link']
    string = "<h1>Page "+url+"</h1>"
    return HttpResponse(string)
