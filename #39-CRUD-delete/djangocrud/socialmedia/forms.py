from django import forms
from .models import SocialMediaModel


class SocialMediaForms(forms.ModelForm):
    class Meta:
        model = SocialMediaModel
        fields = [
            'first_name',
            'last_name',
            'username'
        ]
        labels = {
            'first_name': 'Nama Depan',
            'last_name': 'Nama Belakang',
            'username': 'Username'
        }

        def set_widgets(fields, labels):
            widgets = dict()
            for field in fields:
                widgets[field] = forms.TextInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': 'Masukan ' + labels[field]
                    }
                )
            return widgets

        widgets = set_widgets(fields, labels)
