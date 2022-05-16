from urllib import request
from django import forms
from pkg_resources import require

# Create your forms here


class ContactForm(forms.Form):
    nama_lengkap = forms.CharField(max_length=100)
    GENDER = (
        ('U', 'Unknown'),
        ('P', 'Pria'),
        ('W', 'Wanita'),
    )
    jenis_kelamin = forms.ChoiceField(choices=GENDER)
    email = forms.EmailField(label="Alamat Email")
    alamat = forms.CharField(required=False)
    kode_pos = forms.IntegerField(required=False)
    kota = forms.CharField()
    provinsi = forms.CharField(required=False)
    agreement = forms.BooleanField(label='Pernyataan Setuju')
