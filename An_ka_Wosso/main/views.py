from django.shortcuts import render

from main.models import Product


# Create your views here.

def index(request):
    return render(request, 'index.html')


def product(request):
    all_product = Product.objects.all()
    return render(request, 'product.html', {'products': all_product})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')