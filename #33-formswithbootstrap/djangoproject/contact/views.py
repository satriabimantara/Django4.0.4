from django.shortcuts import render
from .forms import ContactForm

# Create your views here.


def index(request):
    # instansiasi kelas ContactForm
    contact_form = ContactForm()
    context = {
        'title_page': "Contact",
        'sub_title': "Halaman Contact",
        'contact_form': contact_form
    }
    if request.method == "POST":
        context['nama'] = request.POST['nama']
        context['alamat'] = request.POST['alamat']
    return render(request, 'contact/index.html', context)
