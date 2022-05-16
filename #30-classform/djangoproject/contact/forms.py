from django import forms

# Create your forms here


class ContactForm(forms.Form):
    nama = forms.CharField()
    alamat = forms.CharField()
