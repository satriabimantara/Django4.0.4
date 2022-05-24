from django.contrib import admin
from .models import Artikel
# Register your models here.


class ArtikelAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
        'publish_artikel',
        'update_time_artikel'
    ]


admin.site.register(Artikel, ArtikelAdmin)
