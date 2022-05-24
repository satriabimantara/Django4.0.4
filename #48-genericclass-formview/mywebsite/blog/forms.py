from dataclasses import fields
from django import forms
from .models import Artikel


class ArtikelForms(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = [
            'judul_artikel',
            'isi_artikel',
            'penulis_artikel'
        ]
