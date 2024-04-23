from django.shortcuts import render
from .models import *
from Product.models import *


# Create your views here.
def home(request):
    products = Product.objects.all()
    is_fev = Product.objects.filter(is_favorite=True)
    is_new = Product.objects.filter(is_new=True)
    is_pop = Product.objects.filter(is_popular=True)
    is_fet = Product.objects.filter(is_featured=True)
    promo = Promotion.objects.all()
    return render(request, 'Home/homepage.html', locals())