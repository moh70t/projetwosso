from django.urls import include, path 
from .views import index, product, about, contact, add_to_cart, view_cart, checkout, register

urlpatterns = [
    path('', index, name='index'),
    path('product/', product, name='product'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', register, name='register'),
]
