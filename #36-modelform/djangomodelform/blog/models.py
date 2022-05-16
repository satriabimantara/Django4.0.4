from django.db import models

# Create your models here.


class PostModel(models.Model):
    judul = models.CharField(max_length=100)
    body = models.TextField(max_length=300)
    PILIHAN = (
        ('artikel', 'Artikel'),
        ('blog', 'Blog'),
        ('berita', 'Jurnal'),
    )
    category = models.CharField(
        max_length=20,
        choices=PILIHAN,
        default='-'
    )

    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}. {}".format(self.id, self.judul)
