from urllib import request
from django import forms
from pkg_resources import require


"""
Please refers to Form Field and Widget on Google
"""
# Create your forms here


class ContactForm(forms.Form):
    nama_lengkap = forms.CharField(max_length=100)
    GENDER = (
        ('U', 'Unknown'),
        ('P', 'Pria'),
        ('W', 'Wanita'),
    )
    jenis_kelamin = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=GENDER
    )
    TAHUN = range(1945, 2023, 1)
    tanggal_lahir = forms.DateField(
        widget=forms.SelectDateWidget(years=TAHUN),
        label='Birth Date'
    )
    email = forms.EmailField(label="Alamat Email")
    alamat = forms.CharField(
        widget=forms.Textarea,
        max_length=100,
        required=False
    )
    agreement = forms.BooleanField(label='Pernyataan Setuju')
