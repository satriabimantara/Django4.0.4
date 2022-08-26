from django.db import models
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.


class Artikel(models.Model):
    judul = models.CharField(max_length=20)
    isi = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    published = models.DateTimeField(null=True)
    slug = models.SlugField(blank=True, editable=False)

    # mengubah default_permission pada admin dashboard untuk model Blog
    class Meta:
        default_permissions = ('add', 'change', 'delete',)

        # menambahkan custom permission
        permissions = (
            ('publish_artikel', 'Can publish artikel'),
        )

    def save(self):
        self.slug = slugify(self.judul)

        # buat logika ketika is_published bernilai True maka published diset timezone.now
        if self.is_published == True:
            self.published = timezone.now()
        else:
            self.published = None

        super().save()

    def __str__(self):
        return "{}. {}".format(self.id, self.judul)
