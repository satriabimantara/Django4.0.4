from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.


class KategoriArtikel(models.Model):
    nama_kategori = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_kategori


class Artikel(models.Model):
    judul = models.CharField(max_length=244)
    isi = models.TextField()
    kategori = models.ForeignKey(
        KategoriArtikel, on_delete=models.SET_NULL, null=True)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.judul)
        super().save()

    # setelah datanya disave, halamannya mau dilempar kemana dari CreateView?
    def get_absolute_url(self):
        return reverse("artikel:detail", kwargs={"pk": self.id})

    def __str__(self):
        return "{}. {}".format(self.id, self.judul)
