from django.core.exceptions import ValidationError


def validasi_username(username_input):
    if username_input[0] != "@":
        raise ValidationError('Username harus diawali dengan @')
    return username_input
