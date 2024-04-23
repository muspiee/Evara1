from django.shortcuts import render
from .models import *
# Create your views here.

def prod_page(request, id):
    single_prod = Product.objects.get(id=id)
    size = Size.objects.all()
    return render(request, 'products/product_page.html', locals())
