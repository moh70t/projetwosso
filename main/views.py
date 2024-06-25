from django.shortcuts import render, redirect, get_object_or_404

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

    paginator = Paginator(all_product, 5) #10 est le maximum de produit a afficher

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Product.objects.values_list('categorie', flat=True).distinct()

    return render(request, 'product.html', {'page_obj': page_obj, 'query': query, 'categories': categories, 'selected_category': category})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    
    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'product_name': product.nom,
            'price': str(product.prix),
            'quantity': 1
        }
    
    request.session['cart'] = cart
    return redirect('cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    return render(request, 'cart.html', {'cart': cart})

def checkout(request):
    cart = request.session.get('cart', {})
    # Logic for processing payment goes here

    # Clear the cart after purchase
    request.session['cart'] = {}
    return render(request, 'checkout.html', {'cart': cart})


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