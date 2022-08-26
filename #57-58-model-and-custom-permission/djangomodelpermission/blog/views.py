from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

# Create your views here.

# view ini hanya bisa diakses kalau user memiliki permission add_artikel
'''
Kita bisa menumpuk beberapa decorator sekaligus, seperti: 
-@login_required
-@permission_required
dan seterusnya untuk mengecek apapun sekaligus
'''
# @permission_required('blog.add_artikel')
# @permission_required('blog.add_artikel', login_url='/admin/')


@permission_required('blog.add_artikel', login_url=None, raise_exception=True)
def addView(request):
    context = {
        'page_title': 'Blog Add Artikel'
    }
    return render(request, 'blog/add.html', context)


def indexView(request):
    context = {
        'page_title': 'Blog Index',
        'user_permissions': request.user.get_all_permissions()
    }
    return render(request, 'blog/index.html', context)
