from django.urls import include, path
from django.contrib.auth import views as auth_views
from .views import index, login_view, product, about, add_to_cart, cart_detail, checkout, register, generate_invoice, contact_view, contact_success, privacy_policy, terms_of_service, login

urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('', index, name='index'),
    path('product/', product, name='product'),
    path('product/<int:product_id>/add_to_cart/', add_to_cart, name='add_to_cart'),
    path('generate_invoice/', generate_invoice, name='generate_invoice'),
    path('about/', about, name='about'),
    path('contact/', contact_view, name='contact_view'),
    path('contact/success/', contact_success, name='contact_success'),
    path('cart_detail/', cart_detail, name='cart_detail'),
    path('checkout/', checkout, name='checkout'),
    path('privacy/', privacy_policy, name='privacy_policy'),
    path('terms/', terms_of_service, name='terms_of_service'),
    path('accounts/', include('django.contrib.auth.urls')),  # Ajoutons cette ligne pour inclure les vues d'authentification intégrées de Django
    path('accounts/register/', register, name='register'),
]
