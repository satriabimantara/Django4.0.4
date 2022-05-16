from django.db import models
from .validators import validasi_username

# Create your models here.


class SocialMediaModel(models.Model):
    first_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=30)
    username = models.TextField(
        max_length=50,
        validators=[
            validasi_username
        ]
    )

    def __str__(self):
        return "{}. {}".format(self.id, self.username)
