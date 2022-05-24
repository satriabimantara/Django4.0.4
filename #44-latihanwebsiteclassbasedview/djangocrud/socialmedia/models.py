from django.db import models
from .validators import validasi_username

# Create your models here.


class SocialMediaModel(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    username = models.CharField(
        max_length=50,
        validators=[
            validasi_username
        ]
    )
    CONTENT_CATEGORIES = (
        ('programming', 'Programming'),
        ('vlog', 'Vlog'),
        ('culinary', 'Culinary'),
        ('nan', 'Not Set')
    )
    category_content = models.CharField(
        max_length=50,
        choices=CONTENT_CATEGORIES,
        default='nan'
    )

    def __str__(self):
        return "{}. {}".format(self.id, self.username)
