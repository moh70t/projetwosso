from email.message import EmailMessage
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse

from main.models import Product
from django.contrib.auth import login, authenticate
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm, SignUpForm, AddToCartForm
from .models import Product, Cart, CartProduct
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from io import BytesIO
from reportlab.pdfgen import canvas


# Create your views here.

def index(request):
    return render(request, 'index.html')


def product(request):
    query = request.GET.get('q')
    
    category = request.GET.get('category', '')
    all_product = Product.objects.all().order_by('name')

    if query:
        all_product = all_product.filter(name=query)

    if category:
        all_product = all_product.filter(categorie=category)

    paginator = Paginator(all_product, 5) #10 est le maximum de produit a afficher

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Product.objects.values_list('categorie', flat=True).distinct()

    return render(request, 'product.html', {'page_obj': page_obj, 'query': query, 'categories': categories, 'selected_category': category})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     cart, created = Cart.objects.get_or_create(user=request.user)
    
#     if request.method == 'POST':
#         form = AddToCartForm(request.POST)
#         if form.is_valid():
#             quantity = form.cleaned_data['quantity']
#             cart_product, created = CartProduct.objects.get_or_create(cart=cart, product=product)
#             cart_product.quantity += quantity
#             cart_product.save()
#             return redirect('cart')
#     else:
#         form = AddToCartForm(initial={'product_id': product_id})
#         print('Erreur')
    
#     return render(request, 'add_to_cart.html', {'form': form, 'product': product})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_product, created = CartProduct.objects.get_or_create(cart=cart, product=product)
    cart_product.quantity += 1
    cart_product.save()
    return redirect('product_list')


def cart_detail(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'cart_detail.html', {'cart': cart})


def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_products = CartProduct.objects.filter(cart=cart)
    total_price = sum(item.product.price * item.quantity for item in cart_products)
    return render(request, 'checkout.html', {'cart_products': cart_products, 'total_price': total_price})


def process_order(request):
    cart = get_object_or_404(Cart, user=request.user)
    # Traitement de la commande ici
    # Créer un PDF de la commande
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 800, "Détails de la commande")
    y = 750
    for item in CartProduct.objects.filter(cart=cart):
        total_price = sum(item.product.price * item.quantity for item in CartProduct.objects.filter(cart=cart))
        p.drawString(100, y, f"{item.quantity} x {item.product.name} - {item.product.price * item.quantity} FCFA")
        y -= 20
    p.drawString(100, y - 20, f"Total: {total_price} FCFA")
    p.showPage()
    p.save()

    # Envoyer le PDF par email à l'administrateur
    buffer.seek(0)
    email = EmailMessage(
        'Nouvelle commande',
        'Une nouvelle commande a été passée. Veuillez trouver les détails en pièce jointe.',
        settings.DEFAULT_FROM_EMAIL,
        [settings.ADMIN_EMAIL],
    )
    email.attach('commande.pdf', buffer.getvalue(), 'application/pdf')
    email.send()

    # Télécharger le PDF pour le client
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="commande.pdf"'
    return response
    cart.delete()
    return redirect('product_list')


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


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})