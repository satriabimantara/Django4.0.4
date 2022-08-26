from django.contrib import admin
from .models import Artikel
# Register your models here.


class ArtikelAdminPage(admin.ModelAdmin):
    # pindahkan ke dalam function get_readonly_fields
    # readonly_fields = [
    #     'created',
    #     'published',
    #     'updated',
    #     'is_published',
    #     'slug'
    # ]
    # Buat logika untuk group Editor bisa melakukan publish_artikel
    def get_readonly_fields(self, request, obj):
        '''
        request --> berisi request HTTP
        obj --> berisi seluruh data yang tampil di modelAdmin

        ----------
        Ada dua group:
        a. Editor: Change and Publish Artikel
        b. Penulis: Add and Change Artikel

        ----------
        Aturan:
        1. Kalau artikel sudah dipublish, maka artikel tersebut tidak bisa diedit lagi. 

        '''
        current_user_login = request.user

        # cek apakah user memiliki permission tertentu
        is_user_has_add_artikel = current_user_login.has_perm(
            'blog.add_artikel')
        is_user_has_publish_artikel = current_user_login.has_perm(
            'blog.publish_artikel'
        )

        # check apakah obj None atau tidak.
        readonly_fields = [
            'created',
            'published',
            'updated',
            'slug'
        ]
        if obj == None:
            # berarti phase add_artikel (Penulis)
            readonly_fields.append('is_published')
            return readonly_fields
        elif obj != None:
            # berarti phase change_artikel
            if is_user_has_publish_artikel:

                return readonly_fields
            elif is_user_has_add_artikel:
                if obj.is_published:
                    # return semua field yang ada untuk model Artikel
                    return [data.name for data in self.model._meta.fields]
                else:
                    readonly_fields.append('is_published')
                    return readonly_fields


admin.site.register(Artikel, ArtikelAdminPage)
