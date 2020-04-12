from django.shortcuts import render, redirect
from .models import Cart
from Products.models import Product


def carts(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, 'carts/carts.html', {"cart": cart_obj})


def cart_update(request):
    print(request.POST)
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return redirect('carts')
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
    return redirect('carts')
