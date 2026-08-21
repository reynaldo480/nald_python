from django.shortcuts import render
from .models import Product


def store_home(request):
    products = Product.objects.all()

    return render(request, 'store/index.html', {
        'products': products
    })

# Create your views here.
