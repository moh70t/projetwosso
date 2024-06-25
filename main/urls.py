from django.urls import include, path
from .views import index, product, about, add_to_cart, cart_detail, checkout, register, generate_invoice, contact_view, contact_success

urlpatterns = [
    path('', index, name='index'),
    path('product/', product, name='product'),
    path('product/<int:product_id>/add_to_cart/', add_to_cart, name='add_to_cart'),
    path('generate_invoice/', generate_invoice, name='generate_invoice'),
    path('about/', about, name='about'),
    path('contact/', contact_view, name='contact'),
    path('contact/success/', contact_success, name='contact_success'),
    path('cart_detail/', cart_detail, name='cart_detail'),
    path('checkout/', checkout, name='checkout'),
    path('accounts/', include('django.contrib.auth.urls')),  # Ajoutons cette ligne pour inclure les vues d'authentification intégrées de Django
    path('accounts/register/', register, name='register'),
]
