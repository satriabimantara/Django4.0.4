from django.core.exceptions import ValidationError


def validasi_judul(value):
    judul_input = value
    if judul_input == "Post XX":
        raise ValidationError("Judul ini tidak bisa diposting")
