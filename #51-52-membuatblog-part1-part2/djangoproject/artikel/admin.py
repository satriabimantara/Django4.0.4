from django.contrib import admin
from .models import (
    Artikel,
    KategoriArtikel
)
# Register your models here.


class ArtikelAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
        'updated',
        'published'
    ]


admin.site.register(Artikel, ArtikelAdmin)
admin.site.register(KategoriArtikel)
