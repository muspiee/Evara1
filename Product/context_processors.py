from .models import *


def Category_all(request):
    cate = Category.objects.all()
    return {'cate' :cate}
