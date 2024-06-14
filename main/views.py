from django.shortcuts import render

from main.models import Product
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


# Create your views here.

def index(request):
    return render(request, 'index.html')


def product(request):
    query = request.GET.get('q')
    
    category = request.GET.get('category', '')
    all_product = Product.objects.all()

    if query:
        all_product = all_product.filter(name=query)

    if category:
        all_product = all_product.filter(categorie=category)

    paginator = Paginator(all_product, 10) #10 est le maximum de produit a afficher

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Product.objects.values_list('categorie', flat=True).distinct()

    return render(request, 'product.html', {'page_obj': page_obj, 'query': query, 'categories': categories, 'selected_category': category})


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Send an email
            send_mail(
                f'Message from {name}',
                message,
                email,
                [settings.DEFAULT_FROM_EMAIL],
            )
            
            return render(request, 'contact.html', {'form': form, 'success': True})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})