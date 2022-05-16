from urllib import request
from django import forms
from pkg_resources import require


"""
Please refers to Form Field and Widget on Google
"""
# Create your forms here


class ContactForm(forms.Form):
    nama_lengkap = forms.CharField(
        label='Nama Lengkap',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukan nama lengkap'
            }
        )
    )
    GENDER = (
        ('U', 'Unknown'),
        ('P', 'Pria'),
        ('W', 'Wanita'),
    )
    jenis_kelamin = forms.ChoiceField(
        widget=forms.RadioSelect(
            attrs={
                'class': 'form-check-input'
            }
        ),
        choices=GENDER,
        label='Jenis Kelamin'
    )
    TAHUN = range(1945, 2023, 1)
    tanggal_lahir = forms.DateField(
        widget=forms.SelectDateWidget(
            years=TAHUN,
            attrs={
                'class': 'form-control col-sm-2'
            }
        ),
        label='Birth Date'
    )
    email = forms.EmailField(
        label="Alamat Email",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    alamat = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control'
            }
        ),
        max_length=100,
        required=False
    )
    agreement = forms.BooleanField(
        label='Pernyataan Setuju',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input'
            }
        )
    )
