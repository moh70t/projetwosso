from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from main.models import Cart, CartItem

from main.models import Product
from django.contrib.auth import login, authenticate
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm, SignUpForm


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


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'main/cart_detail.html', {'cart_items': cart_items})

def checkout(request):
    cart = request.session.get('cart', {})
    # Logic for processing payment goes here

    # Clear the cart after purchase
    request.session['cart'] = {}
    return render(request, 'checkout.html', {'cart': cart})


def about(request):
    return render(request, 'about.html')

def logout(request):
    return redirect('index')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'main/contact_success.html')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def generate_invoice(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    p.drawString(100, 750, f"Invoice for {request.user.first_name} {request.user.last_name}")

    y = 700
    total = 0
    for item in cart_items:
        p.drawString(100, y, f"{item.product.name} - {item.quantity} x ${item.product.price}")
        total += item.quantity * item.product.price
        y -= 20

    p.drawString(100, y - 20, f"Total: ${total}")
    p.showPage()
    p.save()
    return response