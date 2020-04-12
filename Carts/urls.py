from django.urls import path
from . import views


urlpatterns = [
    path('cart', views.carts, name='carts'),
    path('cart/update/', views.cart_update, name='carts_update'),
]
