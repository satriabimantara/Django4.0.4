from secrets import choice
from django import forms


class PostForm(forms.Form):
    judul = forms.CharField(
        label='Judul Tulisan',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control '
            }
        ),
        max_length=100
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 4
            }
        ),
        label='Isi Tulisan',
        max_length=300,
    )
    PILIHAN = (
        ('', '- kategori -'),
        ('artikel', 'Artikel'),
        ('blog', 'Blog'),
        ('berita', 'Jurnal'),
    )
    category = forms.ChoiceField(
        choices=PILIHAN,
        label='Kategori Blog',
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )

    '''
    Membuat Aturan Validasi untuk form ini
    '''
    # Membuat aturan validasi dari field Judul, harus diawali dengan 'clean_namafield'

    def clean_judul(self):
        # ambil judul_input
        judul_input = self.cleaned_data.get('judul')

        if judul_input == "Post XX":
            raise forms.ValidationError('Judul ini tidak bisa diposting')
        return judul_input
