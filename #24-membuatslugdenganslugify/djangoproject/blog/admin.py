from django.contrib import admin
from .models import Post

# Menampilkan field slug yang hidden karena diset editable false, caranya dengan membuat class


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['slug', ]


# Register your models here.
admin.site.register(Post, PostAdmin)
