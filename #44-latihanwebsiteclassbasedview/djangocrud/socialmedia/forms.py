from django import forms
from .models import SocialMediaModel


class SocialMediaForms(forms.ModelForm):
    class Meta:
        model = SocialMediaModel
        text_input_fields = [
            'first_name',
            'last_name',
            'username',
        ]
        category_input_fields = [
            'category_content'
        ]
        fields = text_input_fields + category_input_fields

        text_input_labels = {
            'first_name': 'Nama Depan',
            'last_name': 'Nama Belakang',
            'username': 'Username',
        }
        category_input_labels = {
            'category_content': "Kategori Konten"
        }
        labels = {}
        labels.update(text_input_labels)
        labels.update(category_input_labels)

        def set_widgets_text_inputs(text_input_fields, text_input_labels):
            widgets = dict()
            for field in text_input_fields:
                widgets[field] = forms.TextInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': 'Masukan ' + text_input_labels[field]
                    }
                )
            return widgets

        def set_widgets_category_inputs(category_input_fields, category_input_labels):
            widgets = dict()
            for field in category_input_fields:
                widgets[field] = forms.Select(
                    attrs={
                        'class': 'form-control',
                    }
                )
            return widgets
        widgets = {}
        widgets.update(set_widgets_text_inputs(
            text_input_fields, text_input_labels))
        widgets.update(set_widgets_category_inputs(
            category_input_fields, category_input_labels))
