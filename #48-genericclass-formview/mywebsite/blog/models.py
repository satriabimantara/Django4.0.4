from django.db import models
from django.utils.text import slugify
# Create your models here.


class Artikel(models.Model):
    judul_artikel = models.CharField(max_length=233)
    isi_artikel = models.TextField(max_length=800)
    penulis_artikel = models.CharField(max_length=100)
    publish_artikel = models.DateTimeField(auto_now_add=True)
    update_time_artikel = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.judul_artikel)
        super(Artikel, self).save()

    def __str__(self):
        return "{}. {}".format(self.id, self.judul_artikel)
